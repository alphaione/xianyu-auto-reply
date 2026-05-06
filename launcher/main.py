"""启动器主入口（最小桩，业务逻辑见 _bootstrap.py）"""
import sys
from pathlib import Path


def _is_frozen_early() -> bool:
    """早期编译模式检测（在 sys.path 设置前使用）"""
    if getattr(sys, "frozen", False):
        return True
    if sys.platform == "win32":
        exe_name = Path(sys.executable).name.lower()
        if exe_name not in ("python.exe", "pythonw.exe", "python3.exe", "python"):
            if not exe_name.startswith("python"):
                return True
    return False


if _is_frozen_early():
    project_root = Path(sys.executable).parent
else:
    project_root = Path(__file__).parent.parent

sys.path.insert(0, str(project_root))

from _bootstrap import main  # noqa: E402

if __name__ == "__main__":
    main()
