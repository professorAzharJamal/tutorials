from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Flatten, Reshape
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

# Define latent noise dimension
noise_dim = 100

def build_generator():
  """
  Defines the generator model that creates digits from noise.
  """
  model = Sequential()
  model.add(Dense(7 * 7 * 256, use_bias=False, input_shape=(noise_dim,)))
  model.add(LeakyReLU(alpha=0.2))
  model.add(Reshape((7, 7, 256)))
  model.add(Conv2DTranspose(128, (3, 3), strides=2, padding='same', activation='relu'))
  model.add(Conv2DTranspose(1, (3, 3), strides=2, padding='same', activation='tanh'))
  return model

def build_discriminator():
  """
  Defines the discriminator model that classifies real vs. generated digits.
  """
  model = Sequential()
  model.add(Conv2D(32, (3, 3), strides=2, padding='same', input_shape=(28, 28, 1)))
  model.add(LeakyReLU(alpha=0.2))
  model.add(Conv2D(64, (3, 3), strides=2, padding='same', activation='relu'))
  model.add(LeakyReLU(alpha=0.2))
  model.add(Flatten())
  model.add(Dense(1, activation='sigmoid'))
  return model

# Create the models
generator = build_generator()
discriminator = build_discriminator()

# Set up for training the generator (freeze discriminator)
discriminator.compile(loss='binary_crossentropy', optimizer=Adam())
discriminator.trainable = False

# Combine models for training generator
gan = Sequential([generator, discriminator])
gan.compile(loss='binary_crossentropy', optimizer=Adam())

# Load MNIST dataset
(X_train, _), (_, _) = mnist.load_data()

# Reshape and normalize data
X_train = X_train.reshape((-1, 28, 28, 1))
X_train = X_train.astype('float32') / 255.0  # Normalize pixel values to [0, 1]

# Training parameters
batch_size = 32
epochs = 10

# Training loop
for epoch in range(epochs):
  # Train discriminator on real and generated digits
  noise = np.random.rand(batch_size, noise_dim)
  fake_digits = generator.predict(noise)

  real_loss = discriminator.train_on_batch(X_train[np.random.randint(0, X_train.shape[0], size=batch_size)], np.ones((batch_size, 1)))
  fake_loss = discriminator.train_on_batch(fake_digits, np.zeros((batch_size, 1)))
  discriminator_loss = (real_loss + fake_loss) / 2

  # Train generator
  discriminator.trainable = False
  noise = np.random.rand(batch_size, noise_dim)
  generator_loss = gan.train_on_batch(noise, np.ones((batch_size, 1)))

  # Print training progress
  print(f"Epoch {epoch+1}/{epochs}, Generator loss: {generator_loss}, Discriminator loss: {discriminator_loss}")

# Generate sample digits after training
noise = np.random.rand(10, noise_dim)
generated_digits = generator.predict(noise)

# Process and visualize the generated digits (replace with your visualization logic)
# Here's an example using matplotlib
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 5, figsize=(10, 4))
for i in range(10):
  axs[i // 5, i % 5].imshow(generated_digits[i, :, :, 0], cmap='gray')
  axs[i // 5, i % 5].axis('off')
plt.tight_layout()
plt.show()
