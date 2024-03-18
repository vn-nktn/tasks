from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def get_product_category_pairs(products_df, categories_df, relations_df):
    # Создаем временные DataFrame для удобства
    temp_df = relations_df.join(products_df, "product_id").join(categories_df, "category_id", "right_outer")

    # Получаем пары "Имя продукта – Имя категории"
    product_category_pairs = temp_df.select("product_name", "category_name")

    # Получаем имена продуктов, у которых нет категорий
    products_without_category = products_df.join(F.broadcast(temp_df), "product_id", "left_outer") \
                                           .filter(F.col("category_id").isNull()) \
                                           .select("product_name")

    # Объединяем результаты
    result_df = product_category_pairs.union(products_without_category.withColumn("category_name", F.lit(None)))

    return result_df

# Пример использования
if __name__ == "__main__":
    # Создаем SparkSession
    spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

    # Примеры DataFrame (замените их на ваши реальные данные)
    products_data = [("product1", 1), ("product2", 2), ("product3", 3)]
    categories_data = [(1, "categoryA"), (2, "categoryB"), (3, "categoryC")]
    relations_data = [("product1", 1), ("product2", 2), ("product3", None)]

    products_df = spark.createDataFrame(products_data, ["product_name", "product_id"])
    categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
    relations_df = spark.createDataFrame(relations_data, ["product_name", "category_id"])

    result = get_product_category_pairs(products_df, categories_df, relations_df)

    result.show()
