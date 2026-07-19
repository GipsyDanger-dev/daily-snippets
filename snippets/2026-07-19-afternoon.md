# TensorFlow.js: Machine Learning di Browser

**Kategori:** Web AI | **Difficulty:** Intermediate | **Session:** Afternoon | **Date:** 2026-07-19

---


## Apa itu TensorFlow.js?

TensorFlow.js adalah library untuk menjalankan **machine learning di browser** dan Node.js. Kamu bisa:
- Train model di browser
- Load model yang sudah di-train (Python)
- Jalankan inference tanpa server

## Install

```bash
# Browser
npm install @tensorflow/tfjs

# Atau via CDN
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
```

## Dasar Tensor

```javascript
// Buat tensor
const t = tf.tensor1d([1, 2, 3, 4, 5]);
console.log(t.shape);  // [5]
console.log(t.dtype);  // float32

// 2D tensor (matrix)
const m = tf.tensor2d([[1, 2], [3, 4]]);
console.log(m.shape);  // [2, 2]

// Operasi
const a = tf.tensor1d([1, 2, 3]);
const b = tf.tensor1d([4, 5, 6]);

const c = a.add(b);      // [5, 7, 9]
const d = a.mul(b);      // [4, 10, 18]
const e = a.mean();      // 2.0

// Cleanup memory
a.dispose();
b.dispose();
c.dispose();

// Atau gunakan tf.tidy()
const result = tf.tidy(() => {
    const a = tf.tensor1d([1, 2, 3]);
    const b = tf.tensor1d([4, 5, 6]);
    return a.add(b);
});  // Auto cleanup
```

## Simple Model

```javascript
// Buat model linear
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

// Compile
model.compile({
    optimizer: 'sgd',
    loss: 'meanSquaredError'
});

// Data training
const xs = tf.tensor1d([1, 2, 3, 4, 5]);
const ys = tf.tensor1d([2, 4, 6, 8, 10]);

// Train
async function train() {
    await model.fit(xs, ys, {
        epochs: 100,
        callbacks: {
            onEpochEnd: (epoch, logs) => {
                console.log(`Epoch ${epoch}: loss = ${logs.loss.toFixed(4)}`);
            }
        }
    });

    // Predict
    const result = model.predict(tf.tensor1d([6]));
    console.log('Prediction:', await result.data());
}

train();
```

## Image Classification

```javascript
async function classifyImage() {
    // Load pretrained model
    const model = await tf.loadLayersModel('path/to/model.json');

    // Load and preprocess image
    const img = document.getElementById('image');
    const tensor = tf.browser.fromPixels(img)
        .resizeBilinear([224, 224])
        .div(255.0)
        .expandDims();

    // Predict
    const predictions = await model.predict(tensor).data();

    // Get top 3 predictions
    const classes = ['Cat', 'Dog', 'Bird'];
    const top3 = Array.from(predictions)
        .map((p, i) => ({class: classes[i], probability: p}))
        .sort((a, b) => b.probability - a.probability)
        .slice(0, 3);

    console.log('Top 3 predictions:', top3);
}
```

## Transfer Learning

```javascript
async function transferLearning() {
    // Load MobileNet as base
    const mobilenet = await tf.loadLayersModel(
        'https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_0.25_224/model.json'
    );

    // Freeze base layers
    mobilenet.layers.forEach(layer => {
        layer.trainable = false;
    });

    // Add custom layers
    const model = tf.sequential();
    model.add(mobilenet);
    model.add(tf.layers.dense({units: 10, activation: 'softmax'}));

    // Compile and train
    model.compile({
        optimizer: 'adam',
        loss: 'categoricalCrossentropy',
        metrics: ['accuracy']
    });

    return model;
}
```

## Browser Integration

```html
<!DOCTYPE html>
<html>
<head>
    <title>ML in Browser</title>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
</head>
<body>
    <input type="file" id="fileInput" accept="image/*">
    <img id="preview" width="224" height="224">
    <p id="result"></p>

    <script>
        document.getElementById('fileInput').addEventListener('change', async (e) => {
            const file = e.target.files[0];
            const img = document.getElementById('preview');
            img.src = URL.createObjectURL(file);

            img.onload = async () => {
                const model = await tf.loadLayersModel('/model.json');
                const tensor = tf.browser.fromPixels(img)
                    .resizeBilinear([224, 224])
                    .div(255.0)
                    .expandDims();

                const prediction = await model.predict(tensor).data();
                document.getElementById('result').textContent =
                    `Prediction: ${(prediction[0] * 100).toFixed(2)}%`;
            };
        });
    </script>
</body>
</html>
```

## Latihan

1. Build digit recognizer (MNIST) yang jalan di browser
2. Buat real-time object detection dengan webcam
3. Train model custom untuk klasifikasi gambar
4. Implement style transfer di browser

## Sumber Belajar

- [TensorFlow.js Official](https://www.tensorflow.org/js)
- [TensorFlow.js Tutorials](https://www.tensorflow.org/js/tutorials)
