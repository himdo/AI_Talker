class ai:
    def __init__ (self,
                  name: str,
                  personality: str,
                  background: str,
                  ai_voice: str):
        '''
        Initializes the AI object
        :param name: The name of the AI
        :param personality: The personality of the AI
        :param background: The background of the AI
        :param ai_voice: The voice of the AI
        '''
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

    def addToLLM_Messages(self, message: str):
        '''
        Adds a message to the list of LLM messages
        :param message: The message to be added
        '''
        self.llm_messages.append(message)

    def getLLM_Messages(self) -> list:
        '''
        Returns the list of LLM messages
        :return: The list of LLM messages
        '''
        return self.llm_messages
    
    def getAI_Voice(self) -> str:
        '''
        Returns the voice of the AI
        :return: The voice of the AI
        '''
        return self.ai_voice
    
    def getAI_Name(self) -> str:
        '''
        Returns the name of the AI
        :return: The name of the AI
        '''
        return self.name
    
    def setLLM_Messages(self, messages: list):
        '''
        Sets the list of LLM messages
        :param messages: The list of LLM messages
        '''
        self.llm_messages = messages