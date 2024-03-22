from setuptools import setup


setup(
        name='autoPlay',     # 包名字
        version='1.0',   # 包版本
        description='auto play mmo',   # 简单描述
        author='Xxx',  # 作者
        python_requires='==3.7',
        install_requires=[
            'thread6==0.2.0',
            'pyHook==1.5.1',
            'pywin32==306',
            'pyUserInput==0.1.10',
            'pyinstaller>=5.13.2',
            'PyScreeze==0.1.30'
            'pyautogui==0.9.54',
            'easyocr==1.7.1',
            'collective.ordereddict==0.1'
            'urllib3==1.25.11'
        ],
        dependency_links = [
            "https://download.lfd.uci.edu/pythonlibs/archived/cp37/pyHook-1.5.1-cp37-cp37m-win_amd64.whl",
            "https://files.pythonhosted.org/packages/80/e6/08192cb5728a6ffdb70ea990d9a1351b320d31a751bb463e652d9e05e7aa/pywin32-306-cp37-cp37m-win_amd64.whl",
        ]
)

