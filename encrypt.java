import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.Key;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Scanner;

public class encrypt {
	static Scanner sc =null;
    public static void main(String[] args) {
    	
        try {
        	sc = new Scanner(System.in);
        	System.out.println("Enter a Value to encrypt : ");
        	String originalText= sc.next();
    	
    		System.out.println("Value of the entered number is "+originalText);
        	
            SecretKey secretKey = generateSecretKey();
     
            String secretKeyString = keyToString(secretKey);
            System.out.println("Secret Key (Base64): " + secretKeyString);

            String[] result = encrypt(originalText, secretKey);
            String encryptedText = result[0];
            String ivString = result[1];

            System.out.println("Encrypted Text: " + encryptedText);
            System.out.println("Initialization Vector (IV) (Base64): " + ivString);

            String decryptedText = decrypt(encryptedText, secretKey, ivString);
            System.out.println("Decrypted Text: " + decryptedText);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static SecretKey generateSecretKey() throws Exception {
        KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
        keyGenerator.init(256); // Use 256-bit key size
        return keyGenerator.generateKey();
    }

    private static String keyToString(Key key) {
        return Base64.getEncoder().encodeToString(key.getEncoded());
    }

    private static String[] encrypt(String plaintext, Key key) throws Exception {
        // Generate a random Initialization Vector (IV)
        SecureRandom secureRandom = new SecureRandom();
        byte[] iv = new byte[16];
        secureRandom.nextBytes(iv);

        // Create IvParameterSpec
        IvParameterSpec ivParameterSpec = new IvParameterSpec(iv);

        // Obtain Cipher instance with CBC mode and IV
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key, ivParameterSpec);

        // Encrypt the plaintext
        byte[] encryptedBytes = cipher.doFinal(plaintext.getBytes());

        // Combine IV and ciphertext and encode to Base64
        byte[] ivAndCiphertext = new byte[iv.length + encryptedBytes.length];
        System.arraycopy(iv, 0, ivAndCiphertext, 0, iv.length);
        System.arraycopy(encryptedBytes, 0, ivAndCiphertext, iv.length, encryptedBytes.length);

        String[] result = new String[2];
        result[0] = Base64.getEncoder().encodeToString(ivAndCiphertext);
        result[1] = Base64.getEncoder().encodeToString(iv);
        return result;
    }

    
    private static String decrypt(String ciphertext, Key key, String ivString) throws Exception {
        // Decode Base64 to get IV and ciphertext
        byte[] ivAndCiphertext = Base64.getDecoder().decode(ciphertext);
        byte[] iv = Base64.getDecoder().decode(ivString);

        // Create IvParameterSpec
        IvParameterSpec ivParameterSpec = new IvParameterSpec(iv);

        // Obtain Cipher instance with CBC mode and IV
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, key, ivParameterSpec);

        // Decrypt the ciphertext
        byte[] decryptedBytes = cipher.doFinal(ivAndCiphertext, iv.length, ivAndCiphertext.length - iv.length);

        return new String(decryptedBytes);
    }
}
