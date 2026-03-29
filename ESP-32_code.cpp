// Pseudocode for the Inference Loop on ESP32
#include <TensorFlowLite.h>

void loop() {
  // 1. Read I2S Microphone Buffer
  read_i2s_data(audio_buffer);

  // 2. Pre-process (FFT/MFCC)
  // This must match your Python 'get_spectrogram' logic exactly!
  generate_features(audio_buffer, feature_tensor);

  // 3. Run Inference
  TfLiteStatus invoke_status = interpreter->Invoke();

  // 4. Hardware Control
  float on_score = output->data.f[0]; // Probability of "ON"
  if (on_score > 0.85) {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("Command: ON");
  }
}
