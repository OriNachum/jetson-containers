from jetson_containers import CUDA_VERSION, IS_SBSA, CUDA_ARCHITECTURES
from packaging.version import Version

def flash_infer(version, version_spec=None, requires=None, default=False):
    pkg = package.copy()

    if requires:
        pkg['requires'] = requires

    pkg['name'] = f'flashinfer:{version}'

    pkg['build_args'] = {
        'FLASHINFER_VERSION': version,
        'FLASHINFER_VERSION_SPEC': version_spec if version_spec else version,
        'TORCH_CUDA_ARCH_LIST': ';'.join([f'{x / 10:.1f}' for x in CUDA_ARCHITECTURES]),
        'IS_SBSA': IS_SBSA,
    }

    builder = pkg.copy()

    builder['name'] = f'flashinfer:{version}-builder'
    builder['build_args'] = {**pkg['build_args'], **{'FORCE_BUILD': 'on'}}

    if default:
        pkg['alias'] = 'flashinfer'
        builder['alias'] = 'flashinfer:builder'

    return pkg, builder


package = [
    flash_infer('0.2.1.post2', '0.2.1.post2', default=False),
    flash_infer('0.2.2', '0.2.2', default=False),
    flash_infer('0.2.2.post1', '0.2.2.post1', default=False),
    flash_infer('0.2.6.post1', '0.2.6.post1', default=(CUDA_VERSION <= Version('12.6'))),
    flash_infer('0.2.7', '0.2.7'),
    flash_infer('0.2.9', '0.2.9', default=(CUDA_VERSION >= Version('12.8'))),
]
