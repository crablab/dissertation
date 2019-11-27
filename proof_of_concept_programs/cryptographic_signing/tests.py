import pytest, random, string
from crypto import crypto

def random_generator(size=32, chars=string.ascii_letters + string.digits):
    """
    Helper function to generate random strings for testing. 
    Based on source: https://pythontips.com/2013/07/28/generating-a-random-string/
    """
    return ''.join(random.choice(chars) for x in range(size))

@pytest.fixture
def cryptoClass():
    return crypto()

def testMatchingSignature(cryptoClass):
    message = random_generator()
    cryptoClass.generate_key()

    signature = cryptoClass.sign_message(message)
    assert(cryptoClass.verify_signature(signature, message))

def testMatchingSignatureDiffKey(cryptoClass):
    message = random_generator()
    cryptoClass.generate_key()

    signature = cryptoClass.sign_message(message)
    cryptoClass.generate_key()
    with pytest.raises(Exception) as e_info:
        cryptoClass.verify_signature(signature, message)
    assert "Signature verification failed" in str(e_info.value)

def testMatchingSignatureDiffMessage(cryptoClass):
    message = random_generator()
    cryptoClass.generate_key()

    signature = cryptoClass.sign_message(message)
    message = random_generator()
    with pytest.raises(Exception) as e_info:
        cryptoClass.verify_signature(signature, message)
    assert "Signature verification failed" in str(e_info.value)

def testMatchingSignatureDiffSignature(cryptoClass):
    signatures = [None] * 2
    messages = [None] * 2

    cryptoClass.generate_key()

    for it, msg in enumerate(messages):
        messages[it] = str(random_generator())
        signatures[it] = cryptoClass.sign_message(messages[it])

    with pytest.raises(Exception) as e_info:
        cryptoClass.verify_signature(signatures[0], messages[1])
    assert "Signature verification failed" in str(e_info.value)