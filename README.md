# FaceMesh dataset creating tool Using google's [mediapipe](https://google.github.io/mediapipe/solutions/face_mesh.html)
## How to use it.

This reposiry contans uses mediapipe model to extract face mesh points from a video file or webcam. The extract points are both 2D(x, y points) and 3D(x, y, z points) points. The extracted mesh is saved with json file format for each frames of the video or webcam feed. If the points are extracted from webcam, the video will also be saved in ``` data/webcam.avi ```. 
<br>
If you want to just visiualize the face mesh without saving the facemesh points, you can also use the code in ``` drawFaceMesh.py ``` file. Here is how you can easily visualize the facemesh using this script.
<br>
Using video file
```shell
$ python drawFaceMesh.py --video_path path/to/video.mp4
```
Using the webcam
```shell
$ python drawFaceMesh.py --camera
```

To save the facemesh points extracted from each frames of the video or webcam, ``` makeDataset.py ``` file. 

From video file, the extracted points will be saved inside ``` data/detected_mesh/videoname ``` folder.
```shell
$ python makedDataset.py --video_path path/to/video.mp4
```

From the webcam, the extracted points will be saved inside ``` data/detected_mesh/webcam ``` folder and the video will be saved in ``` data/webcam.avi ``` file

```shell
$ python makeDataset.py --camera
```

File struecture structure:
``` shell
.
├── ./data
│   └── detected_mesh
│       ├── videoname
│       └── webcam
├── ./log
├── ./utils
│   ├── __init__.py
│   ├── arguement.py
│   └── utils.py
├── cameraFeed.py
├── drawFaceMesh.py
├── faceMesh.py
├── makeDataset.py
├── videoFeed.py
└── README.md
```

## Resources
[Mediapipe](https://google.github.io/mediapipe/solutions/face_mesh.html)
               