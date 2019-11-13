from ecdsa import SigningKey

class crypto:
    """
    A wrapper for the python-ecdsa library. 
    Provides a custom Adaptor for this project
    TODO: remove key getters/setters and provide actual key management
    """

    def generate_key(this):
        """ 
        Generates a NIST192p signature key
        """
        this.sk = SigningKey.generate() 
    
    def get_key(this):
        """
        Returns the current signature key
        :returns: currently loaded key
        """
        return this.sk
    
    def set_key(this, key):
        """
        Sets the current signature key
        :param key: Key to load
        """
        this.sk = key

    def sign_message(this, message):
        """
        Using the signature key signs a given message
        
        :param message: Message to sign 
        :returns: Mesage signature
        """
        if(not this.sk):
            raise Exception("Missing signing key")
        else:
            return this.sk.sign(bytes(message, "UTF-8"))
        
    def verify_signature(this, signature, message):
        """
        Verifies a given signature with the current signature key and message

        :param signature: Signature to verify
        :param message: The message that was signed
        :returns: Boolean indicating valid or not 
        """
        if(not this.sk):
            raise Exception("Missing signing key")
        else:
            vk = this.sk.verifying_key
            return vk.verify(signature, bytes(message, "UTF-8"))