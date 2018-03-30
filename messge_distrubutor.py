from agent_assigner import AgentAssigner
import paho.mqtt.client as mqtt

class MessgeDistributor(object):
    """Handles distributing messages to agents

    Attributes:
        db: the persistance db for the mapping
    """
    def __init__(self):
        """"Creates a new assigner"""
        self.assigner = AgentAssigner()
        
    def distribute_text(self, chat_id, sender_name, text):
        """send a plain text message to the respective agents"""
        topic = self.get_distribution_topic(chat_id)
        print(topic)
        payload = "{}: {}".format(sender_name, text.content.encode('utf-8').strip())
        client.publish(topic, payload)
            
    def get_distribution_topic(self, chat_id):
        """return the topic to allocate a chat to a specific agent"""
        agent_id = self.assigner.get_agent_id(chat_id)
        topic = "{}/{}".format(agent_id, chat_id)
        return topic