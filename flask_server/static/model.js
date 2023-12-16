// static/js/script.js
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Load GLB model
const loader = new THREE.GLTFLoader();
let model;

loader.load("{{ url_for('static', filename='model.glb') }}", (gltf) => {
    model = gltf.scene;
    scene.add(model);
});

// Apply material to the model
const material1_color = 0x1122ff; // Replace with your color
model.traverse((child) => {
    if (child.isMesh) {
        child.material = new THREE.MeshBasicMaterial({ color: material1_color });
    }
});

camera.position.z = 5;

const animate = function () {
    requestAnimationFrame(animate);

    // Add animation or interaction logic here

    renderer.render(scene, camera);
};

animate();
