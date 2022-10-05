from game.casting.actor import Actor

class Artifact(Actor):
    """An artifact is an actor representing a random object with a random message in the screen. 
    
    The responsibility of the artifact is to display messages when the robot is passing through it.

    Attributes:
        _message (string): The message to display
        
    """
    def __ini__(self):
        self._message = ""

    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The artifact's message.
        """ 
        return self._message