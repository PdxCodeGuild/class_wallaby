

console.log('hello world')

const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');
let timer = 1;

function landmarkRecognizer(landmarks) {
  // let tipsArr = []
  // console.log("landmark recog func running")

  // console.log(landmarks)

  try {
    let currentGestureName = document.getElementById('gestureName').innerText
    let announceElem = document.getElementById('matchAnnounce')
    let f = {
      thumb: 4,
      index: 8,
      middle: 12,
      ring: 16,
      pinky: 20
    }

      if (landmarks[0][f.index].y > landmarks[0][f.thumb].y && landmarks[0][f.middle].y > landmarks[0][f.thumb].y && landmarks[0][f.ring].y > landmarks[0][f.thumb].y && landmarks[0][f.pinky].y < landmarks[0][f.thumb].y) {
        console.log('Y')
        if (currentGestureName === 'Y') {
          announceElem.style.display = 'block';
        }
      } else if (landmarks[0][f.index].y > landmarks[0][f.thumb].y) {
        console.log('A')
        if (currentGestureName === 'A') {
          announceElem.style.display = 'block';
        }
      } else if (Math.floor(landmarks[0][f.index].x * 100) === Math.floor(landmarks[0][f.middle].x * 100)) {
        if (currentGestureName === 'C') {
          announceElem.style.display = 'block';
        }
        console.log('C')
      }

  } catch (err) {
    // console.log(err)
  }

  // for (let idx = 4; idx <= 20; idx += 4) {
  //   try {

  //     tipsArr.push(landmarks[0][idx]) //0 for hand 0, only capable of using one hand for now
  //   } catch (err) {
  //     // console.log(err)
  //   }
  // }
  // if (tipsArr.length > 0) {
  //   // console.log(tipsArr)

  // }
}

function onResults(results) {
  canvasCtx.save();
  canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
  canvasCtx.drawImage(
      results.image, 0, 0, canvasElement.width, canvasElement.height);
  if (results.multiHandLandmarks) {
    for (const landmarks of results.multiHandLandmarks) {
      drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS,
                     {color: '#000000', lineWidth: 1});
      drawLandmarks(canvasCtx, landmarks, {color: '#FF0000', lineWidth: 1});

    }
    if (timer === 50) {
      landmarkRecognizer(results.multiHandLandmarks)
      timer = 1;
    }
    timer++;
  }
  canvasCtx.restore();
}

const hands = new Hands({locateFile: (file) => {
  return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
}});
hands.setOptions({
  maxNumHands: 1,
  modelComplexity: 1,
  minDetectionConfidence: 0.5,
  minTrackingConfidence: 0.5
});
hands.onResults(onResults);

const camera = new Camera(videoElement, {
  onFrame: async () => {
    await hands.send({image: videoElement});
  },
  width: 1280,
  height: 720
});
camera.start();

