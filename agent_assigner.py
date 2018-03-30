import shelve

class AgentAssigner(object):
    """Handles the assigning of contacts to agents

    Attributes:
        db: the persistance db for the mapping
    """

    def __init__(self, location = '/home/user/storedb'):
        """Return a new Agent Assigner object."""        
        db = shelve.open(location) 
        self.db = db
  
    def assign_chat(self, chat_id, agent_id):
        """Assign a chat_id to a particular agent"""
        print("Assigning {} to {}".format(chat_id, agent_id))
        self.db[chat_id] = agent_id
        
    def get_agent_id(self, chat_id):
        try:
            agent_id = "no-agent"
            agent_id = self.db[chat_id.encode("utf-8")]
        except KeyError:
            print("No assigned agent found for {}".format(chat_id))    
        finally:
            return agent_id
        
    def close(self):
        print("Exiting Assigner and closing db")
        self.db.close();