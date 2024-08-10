class ai:
    def __init__ (self,
                  name,
                  personality,
                  background):
        self.name = name
        self.personality = personality
        self.background = background
        self.llm_messages = []
        systemMessage = {
            "role":"system",
            "content": f"""
                Your name is {name}.

                Your background is:
                {background}

                Your personality is:
                {personality}

                Everything you say has to be aligned with your personality. All responses have to be short and stay in character.
            """
        }
        self.llm_messages.append(systemMessage)

    def addToLLM_Messages(self, message):
        self.llm_messages.append(message)

    def getLLM_Messages(self):
        return self.llm_messages
