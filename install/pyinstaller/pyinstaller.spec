# -*- mode: python -*-
import sys
import os
import inspect
import platform

p = platform.system()

# Get the version
root = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    )
)
sys.path.insert(0, root)
import dangerzone

version = dangerzone.dangerzone_version
print("Flock Agent version: {}".format(version))

if p == "Darwin":
    datas = [("../../share", "share"), ("../macos/document.icns", ".")]
else:
    datas = [("../../share", "share")]

if p == "Windows":
    icon = os.path.join(root, "share", "dangerzone.ico")
else:
    icon = None

a = Analysis(
    ["dangerzone"],
    pathex=["."],
    binaries=None,
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name="dangerzone",
    debug=False,
    strip=False,
    upx=True,
    console=False,
    icon=icon,
)

coll = COLLECT(
    exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, name="dangerzone"
)

# The macOS app bundle
if p == "Darwin":
    app = BUNDLE(
        coll,
        name="Dangerzone.app",
        icon="dangerzone.icns",
        bundle_identifier="media.firstlook.dangerzone",
        info_plist={
            "NSHighResolutionCapable": True,
            "CFBundleShortVersionString": version,
            "CFBundleDocumentTypes": [
                {
                    "CFBundleTypeExtensions": ["pdf"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": ["application/pdf"],
                    "CFBundleTypeName": "PDF Document",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["docx", "doc"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": [
                        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        "application/msword",
                    ],
                    "CFBundleTypeName": "Microsoft Word Document",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["xlsx", "xls"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": [
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        "application/vnd.ms-excel",
                    ],
                    "CFBundleTypeName": "Microsoft Excel Document",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["pptx", "ppt"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": [
                        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        "application/vnd.ms-powerpoint",
                    ],
                    "CFBundleTypeName": "Microsoft PowerPoint Document",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["odg"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": [
                        "application/vnd.oasis.opendocument.text"
                    ],
                    "CFBundleTypeName": "ODF Text Document",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["ops"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": [
                        "application/vnd.oasis.opendocument.spreadsheet"
                    ],
                    "CFBundleTypeName": "ODF Spreadsheet Document",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["odp"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": [
                        "application/vnd.oasis.opendocument.presentation"
                    ],
                    "CFBundleTypeName": "ODF Presentation Document",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["odg"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": [
                        "application/vnd.oasis.opendocument.graphics"
                    ],
                    "CFBundleTypeName": "ODF Graphics Document",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["jpg", "jpeg"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": ["image/jpeg"],
                    "CFBundleTypeName": "JPEG Image",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["gif"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": ["image/gif"],
                    "CFBundleTypeName": "GIF Image",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["png"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": ["image/png"],
                    "CFBundleTypeName": "PNG Image",
                    "CFBundleTypeRole": "Viewer",
                },
                {
                    "CFBundleTypeExtensions": ["tif", "tiff"],
                    "CFBundleTypeIconFile": "document.icns",
                    "CFBundleTypeMIMETypes": ["image/tiff", "image/x-tiff"],
                    "CFBundleTypeName": "TIFF Image",
                    "CFBundleTypeRole": "Viewer",
                },
            ],
        },
    )