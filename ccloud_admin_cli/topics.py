from ccloud_admin_cli.admin import CCloudAdminClient
import openapi_client


class TopicManager(CCloudAdminClient):

    def __init__(self, api_key, api_secret):
        super().__init__(api_key, api_secret)

    def list_topics(self, cluster_id):
        with openapi_client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.TopicV3Api(api_client)
            cluster_id = cluster_id
            try:
                # List Topics
                topic_data_list = api_instance.list_kafka_topics(cluster_id)
                print("The response of TopicV3Api->list_kafka_topics:\n")
                return [topic_data.topic_name for topic_data in topic_data_list.data if not topic_data.topic_name.startswith('_')]
            except Exception as e:
                print("Exception when calling TopicV3Api->list_kafka_topics: %s\n" % e)
            return []

    def create_topic(self, cluster_id, topic, num_partitions=12, replication_factor=3):
        with openapi_client.ApiClient(self.configuration) as api_client:

            api_instance = openapi_client.TopicV3Api(api_client)
            create_topic_request_data = {"topic_name": topic, "partitions_count": num_partitions,
                                         "replication_factor": replication_factor,
                                         "configs": [{"name": "cleanup.policy", "value": "compact"},
                                                     {"name": "compression.type",
                                                      "value": "gzip"}]}
            try:
                api_response = api_instance.create_kafka_topic(cluster_id,
                                                               create_topic_request_data=create_topic_request_data)
                print("The response of TopicV3Api->create_kafka_topic:\n")
                print(api_response)
            except Exception as e:
                print("Exception when calling TopicV3Api->create_kafka_topic: %s\n" % e)

    def delete_topic(self, cluster_id, topic):
        with openapi_client.ApiClient(self.configuration) as api_client:
            api_instance = openapi_client.TopicV3Api(api_client)
            try:
                api_instance.delete_kafka_topic(cluster_id, topic)
            except Exception as e:
                print("Exception when calling TopicV3Api->delete_kafka_topic: %s\n" % e)