from ccloud_admin_cli.model import ResourceApi
from ccloud_admin_cli.topics import TopicManager


def desired_topic_list(resources):
    the_list = []
    context_container = resources.service["context"]
    for project in resources.service["projects"]:
        project_name = project["name"]
        for topic in project["topics"]:
            topic_name = topic["name"]
            complete_name = f"{context_container}.{project_name}.{topic_name}"
            the_list.append(complete_name)
    return the_list


if __name__ == '__main__':
    api_key = "<API-KEY>"
    api_secret = "<API-SECRET>"
    cluster_id = "<CLUSTER-ID>"

    tm = TopicManager(api_key=api_key, api_secret=api_secret)

    resources = ResourceApi()
    resources.open(resource_file="formular.yaml")

    existing_topics = tm.list_topics(cluster_id=cluster_id)
    desired_topic_list = desired_topic_list(resources)
    topics_to_be_created = list(set(desired_topic_list) - set(existing_topics))
    topics_to_be_deleted = list(set(existing_topics) - set(desired_topic_list))

    for topic_to_delete in topics_to_be_deleted:
        print(f"Deleting topic name {topic_to_delete}")
        tm.delete_topic(cluster_id=cluster_id, topic=topic_to_delete)
    for new_topic in topics_to_be_created:
        print(f"Creating topic name {new_topic}")
        tm.create_topic(cluster_id=cluster_id, topic=new_topic)
