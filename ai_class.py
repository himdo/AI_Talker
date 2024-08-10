class ai:
    def __init__ (self,
                  name,
                  personality,
                  background,
                  ai_voice):
        self.name = name
        self.personality = personality
        self.background = background
        self.ai_voice = ai_voice
        self.llm_messages = []
        systemMessage = {
            "role":"system",
            "content": f"""
                Your name is {name}.

                Your background is:
                {background}

                Your personality is:
                {personality}

                Everything you say has to be aligned with your personality. All responses have to be short and stay in character. No matter what you must only speak as {name} and no one else.
                Your messages MUST begin with "[{name}] "
            """
        }
        self.llm_messages.append(systemMessage)

    def addToLLM_Messages(self, message):
        self.llm_messages.append(message)

    def getLLM_Messages(self):
        return self.llm_messages
    
    def getAI_Voice(self):
        return self.ai_voice
    
    def getAI_Name(self):
        return self.name
    
    def setLLM_Messages(self, messages):
        self.llm_messages = messages