# gsplat

> [`CONTAINERS`](#user-content-containers) [`IMAGES`](#user-content-images) [`RUN`](#user-content-run) [`BUILD`](#user-content-build)

<details open>
<summary><b><a id="containers">CONTAINERS</a></b></summary>
<br>

| **`gsplat:1.5.3`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Aliases | `gsplat` |
| &nbsp;&nbsp;&nbsp;Requires | `L4T ['>=34.1.0']` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build/build-essential) [`pip_cache:cu126`](/packages/cuda/cuda) [`cuda:12.6`](/packages/cuda/cuda) [`cudnn`](/packages/cuda/cudnn) [`python`](/packages/build/python) [`numpy`](/packages/numeric/numpy) [`cmake`](/packages/build/cmake/cmake_pip) [`onnx`](/packages/ml/onnx) [`pytorch:2.8`](/packages/pytorch) [`torchvision`](/packages/pytorch/torchvision) [`torchaudio`](/packages/pytorch/torchaudio) [`tinycudann`](/packages/3d/3dvision/tinycudann) [`torch`](/packages/pytorch) [`ffmpeg`](/packages/multimedia/ffmpeg) [`ninja`](/packages/build/ninja) [`opengl`](/packages/multimedia/opengl) [`pyceres`](/packages/3d/3dvision/pyceres) [`pycolmap`](/packages/3d/3dvision/pycolmap) [`nerfview`](/packages/3d/gaussian_splatting/nerfview) |
| &nbsp;&nbsp;&nbsp;Dependants | [`fruitnerf:1.0`](/packages/3d/nerf/fruitnerf) [`nerfstudio:1.1.7`](/packages/3d/nerf/nerfstudio) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile`](Dockerfile) |
| &nbsp;&nbsp;&nbsp;Notes | https://github.com/nerfstudio-project/gsplat |

</details>

<details open>
<summary><b><a id="run">RUN CONTAINER</a></b></summary>
<br>

To start the container, you can use [`jetson-containers run`](/docs/run.md) and [`autotag`](/docs/run.md#autotag), or manually put together a [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) command:
```bash
# automatically pull or build a compatible container image
jetson-containers run $(autotag gsplat)

# or if using 'docker run' (specify image and mounts/ect)
sudo docker run --runtime nvidia -it --rm --network=host gsplat:36.4.0

```
> <sup>[`jetson-containers run`](/docs/run.md) forwards arguments to [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) with some defaults added (like `--runtime nvidia`, mounts a `/data` cache, and detects devices)</sup><br>
> <sup>[`autotag`](/docs/run.md#autotag) finds a container image that's compatible with your version of JetPack/L4T - either locally, pulled from a registry, or by building it.</sup>

To mount your own directories into the container, use the [`-v`](https://docs.docker.com/engine/reference/commandline/run/#volume) or [`--volume`](https://docs.docker.com/engine/reference/commandline/run/#volume) flags:
```bash
jetson-containers run -v /path/on/host:/path/in/container $(autotag gsplat)
```
To launch the container running a command, as opposed to an interactive shell:
```bash
jetson-containers run $(autotag gsplat) my_app --abc xyz
```
You can pass any options to it that you would to [`docker run`](https://docs.docker.com/engine/reference/commandline/run/), and it'll print out the full command that it constructs before executing it.
</details>
<details open>
<summary><b><a id="build">BUILD CONTAINER</b></summary>
<br>

If you use [`autotag`](/docs/run.md#autotag) as shown above, it'll ask to build the container for you if needed.  To manually build it, first do the [system setup](/docs/setup.md), then run:
```bash
jetson-containers build gsplat
```
The dependencies from above will be built into the container, and it'll be tested during.  Run it with [`--help`](/jetson_containers/build.py) for build options.
</details>
