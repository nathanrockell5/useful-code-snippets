function Marker(){
    THREE.Object3D.call(this)
    var radius = 0.005;
    var sphereRadius = 0.02;
    var height = 0.05;
  
      var material = new THREE.MeshPhongMaterial({ color: 0xbab68f });
  
      var cone = new THREE.Mesh(new THREE.ConeBufferGeometry(radius, height, 8, 1, true), material);
      cone.position.y = height * 0.5;
      cone.rotation.x = Math.PI;
  
      var sphere = new THREE.Mesh(new THREE.SphereBufferGeometry(sphereRadius, 16, 8), material);
      sphere.position.y = height * 0.95 + sphereRadius;
      this.add(cone, sphere);
      Marker.prototype = Object.create(THREE.Object3D.prototype);
  }
  
  function Earth(radius, texture) {
    THREE.Object3D.call(this)
    this.userData.radius = radius
    var earth = new THREE.Mesh(
          new THREE.SphereBufferGeometry(radius, 64.0, 48.0),
          new THREE.MeshPhongMaterial({
              map: texture
          })
      );
      this.add(earth)
    }
      Earth.prototype = Object.create(THREE.Object3D.prototype);
      Earth.prototype.createMarker = function (lat, lon) {
        var marker = new Marker();
        var latRad = lat * (Math.PI / 180);
        var lonRad = -lon * (Math.PI / 180);
        var r = this.userData.radius;
        marker.position.set(Math.cos(latRad) * Math.cos(lonRad) * r, Math.sin(latRad) * r, Math.cos(latRad) * Math.sin(lonRad) * r);
        marker.rotation.set(0.0, -lonRad, latRad - Math.PI * 0.5);
        this.add(marker);
  };
  
  var scene, camera, renderer;
  var controls;
  
  init();
  
  function init() {
      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(45, 4 / 3, 0.1, 100);
      camera.position.set(0.0, 1.5, 3.0);
      renderer = new THREE.WebGLRenderer({ antialias: true });
      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.autoRotate = true;
      controls.autoRotateSpeed = -1.0;
      controls.enablePan = false;
  
      var manager = createLoader(renderer.domElement, animate);
  
      var texLoader = new THREE.TextureLoader(manager).setCrossOrigin(true);
  
      var texture = texLoader.load('./img/map.jpeg');
      texture.anisotropy = renderer.capabilities.getMaxAnisotropy();
  
      var earth = new Earth(1.0, texture);
  }
  
    function animate() {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
  }