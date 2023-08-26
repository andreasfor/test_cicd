# Databricks notebook source
# MAGIC %md
# MAGIC ## Note
# MAGIC
# MAGIC If the test is run from the CLI or with dbutils.notebook.run, do not forget to uncomment 'result.exit(dbutils)' after locally testing. So is is NOT commented out here in order for test_run_all_tests to work. 

# COMMAND ----------

from runtime.nutterfixture import NutterFixture, tag

class MyTestFixture(NutterFixture):

    def assertion_import_basics(self) -> None:
        """
        This is a test
        """
        try:
            from addition import addition_two_numbers
            z = addition_two_numbers(2,5)
            assert z == 7
        except:
            assert False

result = MyTestFixture().execute_tests()
print(result.to_string())
# Comment out the next line (result.exit(dbutils)) to see the test result report from within the notebook
result.exit(dbutils)

# COMMAND ----------

# MAGIC %sh
# MAGIC # pip install nutter
# MAGIC
# MAGIC # export DATABRICKS_HOST=https://adb-4821230018992413.13.azuredatabricks.net
# MAGIC # export DATABRICKS_TOKEN=dapi88db6a2de5efa0fc1955cba77c061479-2
# MAGIC
# MAGIC # nutter run /Repos/andreas.forsberg@capgemini.com/test_cicd/dev_dir/nutter_test --cluster_id 0826-123427-50uwyk9k -timeout 100

# COMMAND ----------


