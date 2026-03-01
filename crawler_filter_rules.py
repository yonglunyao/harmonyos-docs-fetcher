#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档爬取过滤规则
避免爬取已废弃/停止维护的文档
"""

# 需要跳过的目录关键词
SKIP_DIR_KEYWORDS = [
    "已停止维护",
    "已废弃",
    "deprecated",
    "废弃的",
]

# 需要跳过的文件关键词
SKIP_FILE_KEYWORDS = [
    "deprecated",
    "已废弃",
    "已停止维护",
]

# 需要跳过的完整API模块名
SKIP_API_MODULES = {
    # ArkUI 已废弃组件
    "@ohos.navigator",
    "NavRouter",
    "GridContainer",
    "Stepper",
    "StepperItem",
    "Panel (旧版)",

    # System 已废弃模块
    "@system.app",
    "@system.router",
    "@system.prompt",
    "@system.configuration",
    "@system.mediaquery",
    "@system.file",
    "@system.storage",
    "@system.fetch",
    "@system.network",
    "@system.brightness",
    "@system.device",
    "@system.request",
    "@system.sensor",
    "@system.vibrate",
    "@system.notification",
    "@system.cipher",
    "@system.geolocation",

    # 应用框架已废弃模块
    "@ohos.bundle",
    "@ohos.bundle.bundleInfo",
    "@ohos.bundle.elementName",
    "@ohos.bundle.moduleInfo",
    "@ohos.commonEvent",
    "@ohos.notification",
    "@ohos.geolocation",
    "@ohos.faultLogger",
    "@ohos.prompt",
    "@ohos.bluetooth.bluetoothManager",
    "@ohos.bluetoothManager",
    "@ohos.wifiext",
    "@ohos.wantAgent",
    "@ohos.ability.dataUriUtils",
    "@ohos.ability.wantConstant",
    "@ohos.application.Configuration",
    "@ohos.application.Want",
    "@ohos.application.appManager",
    "@ohos.application.formError",
    "@ohos.application.formBindingData",

    # 数据存储已废弃
    "@ohos.data.storage",
    "@ohos.fileio",
    "@ohos.statfs",
    "@ohos.document",

    # 媒体已废弃
    "AudioPlayer (deprecated)",
    "VideoPlayer (deprecated)",
}

# 在爬取时使用的过滤函数
def should_skip_doc(url: str, title: str, category_path: list) -> bool:
    """
    判断是否应该跳过某个文档

    Args:
        url: 文档URL
        title: 文档标题
        category_path: 分类路径列表

    Returns:
        True表示跳过，False表示爬取
    """
    # 检查URL中的关键词
    for keyword in SKIP_DIR_KEYWORDS + SKIP_FILE_KEYWORDS:
        if keyword.lower() in url.lower():
            return True

    # 检查标题中的关键词
    for keyword in SKIP_FILE_KEYWORDS:
        if keyword in title:
            return True

    # 检查分类路径
    for path in category_path:
        for keyword in SKIP_DIR_KEYWORDS:
            if keyword in path:
                return True

    # 检查是否是已废弃的API模块
    for skip_module in SKIP_API_MODULES:
        if skip_module.lower() in title.lower():
            return True

    return False


# 在爬取时的示例用法
"""
if should_skip_doc(doc_url, doc_title, category_paths):
    print(f"跳过废弃文档: {doc_title}")
    continue
"""
