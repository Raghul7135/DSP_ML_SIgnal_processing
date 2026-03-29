import tensorflow as tf
from tensorflow.keras import layers, models

def get_spectrogram(waveform):
    # Convert waveform to a spectrogram via STFT (Short-Time Fourier Transform)
    spectrogram = tf.signal.stft(waveform, frame_length=255, frame_step=128)
    spectrogram = tf.abs(spectrogram)
    # Add a 'channels' dimension for the CNN
    return spectrogram[..., tf.newaxis]

def create_model(input_shape, num_labels):
    model = models.Sequential([
        layers.Input(shape=input_shape),
        # Downsample the input
        layers.Resizing(32, 32),
        layers.Normalization(),
        
        # CNN Layers
        layers.Conv2D(32, 3, activation='relu'),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.25),
        layers.Flatten(),
        
        # Output Layer
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_labels, activation='softmax'),
    ])
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=['accuracy'],
    )
    return model

# Example usage:
# If your spectrogram shape is (124, 129, 1) and you have 4 commands
# model = create_model((124, 129, 1), 4)
# model.summary()
