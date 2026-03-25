#!/usr/bin/env python3
"""
微信公众号文章发布工具（Knowledge-Base 主题版）
作者：黑白交织
样式：基于 Knowledge-Base.css
"""

import sys
import requests
import json
import time
import os
import tempfile

# 配置
APPID = 'wx50ccea6fe909ee09'
SECRET = 'd948e42096116e4d2d78ba262b881a90'
TOKEN_FILE = '/tmp/wechat_token.json'

def get_access_token():
    """获取 stable_access_token"""
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if time.time() < data.get('expires_at', 0):
                    return data['access_token']
        except:
            pass
    
    url = 'https://api.weixin.qq.com/cgi-bin/stable_token'
    data = {
        'grant_type': 'client_credential',
        'appid': APPID,
        'secret': SECRET,
        'force_refresh': False
    }
    resp = requests.post(url, json=data, timeout=10)
    result = resp.json()
    
    if 'access_token' in result:
        result['expires_at'] = time.time() + 7000
        with open(TOKEN_FILE, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)
        return result['access_token']
    else:
        raise Exception(f"Token 获取失败：{result}")

def upload_cover_image(image_path):
    """上传指定封面图"""
    token = get_access_token()
    
    if not os.path.exists(image_path):
        print(f"❌ 图片文件不存在：{image_path}")
        return None
    
    url = f'https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image'
    with open(image_path, 'rb') as f:
        files = {'media': f}
        resp = requests.post(url, files=files, timeout=30)
    
    result = resp.json()
    
    if 'media_id' in result:
        print(f"✅ 封面图上传成功")
        print(f"   media_id: {result['media_id'][:30]}...")
        return result['media_id']
    else:
        print(f"❌ 封面图上传失败：{result}")
        return None

def create_wechat_article_kb_style():
    """创建 Knowledge-Base 风格的文章内容"""
    
    content = f'''<section id="wemd" style="padding: 30px 24px; max-width: 677px; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', 'PingFang SC', sans-serif; color: #37352F; word-break: break-word;">

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">
<strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">摘要：</strong>300 秒→5 秒（57 倍提升），70%→100%（+30%），2 小时→10 分钟（12 倍）。这是一个三人股票交易团队的真实转型故事。
</p></section></section>

<section><h1 style="margin-top: 50px; margin-bottom: 40px; text-align: left; border-bottom: 1px solid #E3E2E0; padding-bottom: 20px;"><span class="content" style="font-size: 28px; font-weight: 700; color: #37352F; display: inline-block; line-height: 1.2;">01 引言</span></h1></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">凌晨 2 点，我还在办公室。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">屏幕上，选股脚本的进度条卡在 87%，已经跑了 280 秒。按照这个速度，等它跑完，市场早就收盘了。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">这已经是本周第 3 次超时，第 5 次临时加班。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">那一刻，我意识到：<strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">我们需要的不是更努力的加班，而是更好的管理方法。</strong></p></section></section>

<section><h2 style="margin-top: 40px; margin-bottom: 20px; text-align: left;"><span class="content" style="display: block; font-size: 22px; font-weight: 600; color: #37352F; padding: 8px 12px; background-color: #F7F6F3; border-radius: 4px; line-height: 1.3;">02 团队介绍</span></h2></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">九章快手团队成立于 2026 年 3 月，交易策略是"一夜持股法"——当天买入，次日卖出。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">三人分工：</strong></p></section></section>

<section><section><table style="width: 100%; border-collapse: collapse; margin: 30px 0; font-size: 14px; border: 1px solid #E3E2E0; border-radius: 0;">
<tr><th style="background: #F7F6F3; color: #37352F; font-weight: 600; border: 1px solid #E3E2E0; padding: 10px 12px; text-align: left;">角色</th><th style="background: #F7F6F3; color: #37352F; font-weight: 600; border: 1px solid #E3E2E0; padding: 10px 12px; text-align: left;">成员</th><th style="background: #F7F6F3; color: #37352F; font-weight: 600; border: 1px solid #E3E2E0; padding: 10px 12px; text-align: left;">职责</th></tr>
<tr><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">组长</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">九章快手</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">交易执行、风险控制、团队管理</td></tr>
<tr><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">策略主管</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">短线快刀客</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">选股策略、脚本开发</td></tr>
<tr><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">股票池主管</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">股海判官</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">候选池维护、基本面研究</td></tr>
</table></section></section>

<section><h2 style="margin-top: 40px; margin-bottom: 20px; text-align: left;"><span class="content" style="display: block; font-size: 22px; font-weight: 600; color: #37352F; padding: 8px 12px; background-color: #F7F6F3; border-radius: 4px; line-height: 1.3;">03 遇到的挑战</span></h2></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">痛点一：任务不清晰</strong></p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">每天早上花 15 分钟互相询问任务，重要任务容易被忽略。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">痛点二：进度不透明</strong></p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">"大概做了一半吧""应该快好了"——模糊的汇报让我们无法及时发现延期风险。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">痛点三：责任不明确</strong></p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">有一次，候选股票池没有及时更新，问了一圈才发现这个任务"悬空"了，没人负责。</p></section></section>

<section><section><div class="multiquote-1" style="margin: 24px 0; padding: 16px 16px 16px 20px; background-color: #F1F1EF; border: none; border-radius: 4px; border-left: 4px solid #37352F; overflow: visible !important;">
<p style="margin: 0; color: #37352F; font-size: 15px; line-height: 1.6;">"没有明确负责人的任务，就像没有主人的狗——没人管。"</p>
</div></section></section>

<section><h2 style="margin-top: 40px; margin-bottom: 20px; text-align: left;"><span class="content" style="display: block; font-size: 22px; font-weight: 600; color: #37352F; padding: 8px 12px; background-color: #F7F6F3; border-radius: 4px; line-height: 1.3;">04 解决方案</span></h2></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">方案一：工作看板</strong></p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">简单说，就是一块"板子"，上面写着所有任务、负责人、进度、状态。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">核心要素：</strong></p></section></section>

<section><section><ul style="list-style-type: disc; padding-left: 24px; margin: 16px 0; color: #37352F;">
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;">任务分级：P0/P1/P2/P3 四个优先级</section></li>
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;">状态管理：待执行/进行中/已完成/阻塞/逾期</section></li>
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;">进度追踪：0%-100% 百分比</section></li>
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;">责任到人：每个任务有明确负责人</section></li>
</ul></section></section>

<section><h2 style="margin-top: 40px; margin-bottom: 20px; text-align: left;"><span class="content" style="display: block; font-size: 22px; font-weight: 600; color: #37352F; padding: 8px 12px; background-color: #F7F6F3; border-radius: 4px; line-height: 1.3;">05 实施效果</span></h2></section>

<section><section><table style="width: 100%; border-collapse: collapse; margin: 30px 0; font-size: 14px; border: 1px solid #E3E2E0; border-radius: 0;">
<tr><th style="background: #F7F6F3; color: #37352F; font-weight: 600; border: 1px solid #E3E2E0; padding: 10px 12px; text-align: left;">指标</th><th style="background: #F7F6F3; color: #37352F; font-weight: 600; border: 1px solid #E3E2E0; padding: 10px 12px; text-align: left;">使用前</th><th style="background: #F7F6F3; color: #37352F; font-weight: 600; border: 1px solid #E3E2E0; padding: 10px 12px; text-align: left;">使用后</th><th style="background: #F7F6F3; color: #37352F; font-weight: 600; border: 1px solid #E3E2E0; padding: 10px 12px; text-align: left;">提升</th></tr>
<tr><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">任务确认时间</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">15 分钟/天</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">1 分钟/天</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">15 倍</td></tr>
<tr><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">重复工作时间</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">2 小时/天</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">&lt;10 分钟/天</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">12 倍</td></tr>
<tr><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">选股脚本时间</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">&gt;300 秒</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">5 秒</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">57 倍</td></tr>
<tr><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">任务按时完成率</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">70%</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">100%</td><td style="border: 1px solid #E3E2E0; padding: 10px 12px; color: #37352F; background: #fff;">+30%</td></tr>
</table></section></section>

<section><h2 style="margin-top: 40px; margin-bottom: 20px; text-align: left;"><span class="content" style="display: block; font-size: 22px; font-weight: 600; color: #37352F; padding: 8px 12px; background-color: #F7F6F3; border-radius: 4px; line-height: 1.3;">06 经验总结</span></h2></section>

<section><section><ul style="list-style-type: disc; padding-left: 24px; margin: 16px 0; color: #37352F;">
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">真实性原则</strong> - 进度真实，不夸大</section></li>
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">及时性原则</strong> - 状态变化后立即更新</section></li>
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">完整性原则</strong> - 必填字段无遗漏</section></li>
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">持续优化</strong> - 每周 Review，每月复盘</section></li>
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">工具服务于人</strong> - 最好的工具不是最贵的，而是最适合的</section></li>
<li style="margin-bottom: 8px; line-height: 1.7;"><section style="color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px;">自动化 + 人工决策</strong> - 95% 自动化，5% 人工决策</section></li>
</ul></section></section>

<section><section><div class="multiquote-1" style="margin: 24px 0; padding: 16px 16px 16px 20px; background-color: #F1F1EF; border: none; border-radius: 4px; border-left: 4px solid #37352F; overflow: visible !important;">
<p style="margin: 0; color: #37352F; font-size: 15px; line-height: 1.6;">"看板本身不会创造价值，使用看板的人才会。"</p>
</div></section></section>

<section><h2 style="margin-top: 40px; margin-bottom: 20px; text-align: left;"><span class="content" style="display: block; font-size: 22px; font-weight: 600; color: #37352F; padding: 8px 12px; background-color: #F7F6F3; border-radius: 4px; line-height: 1.3;">07 结语</span></h2></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">好的管理不是束缚，而是让每个人都能发挥最大的价值。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: justify; color: #37352F; font-size: 16px;">工作看板是我们的"导航仪"，自动化技术是我们的"加速器"。</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: center; color: #37352F; font-size: 16px;"><strong style="color: #37352F; font-weight: 600; background-color: #FDECC8; padding: 2px 4px; margin: 0 2px; border-radius: 3px; font-size: 16px;">一个人可以走得很快，但一群人才能走得很远。</strong></p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: center; color: #37352F; font-size: 16px;">黑白</p></section></section>

<section><section><p style="margin-top: 16px; margin-bottom: 16px; line-height: 1.75; letter-spacing: 0.2px; text-align: center; color: #37352F; font-size: 16px;">2026 年 3 月</p></section></section>

</section>'''
    
    return content

def create_draft(title, content, summary, thumb_media_id):
    """创建草稿"""
    token = get_access_token()
    url = f'https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}'
    
    data = {
        'articles': [{
            'title': title,
            'author': '黑白',  # 作者名（微信限制 20 字节）
            'digest': summary,
            'content': content,
            'thumb_media_id': thumb_media_id,
            'show_cover_pic': 1
        }]
    }
    
    print(f"📤 发送请求...")
    print(f"   标题：{title}")
    print(f"   作者：黑白")
    print(f"   摘要：{summary}")
    print(f"   内容长度：{len(content)}")
    
    resp = requests.post(url, json=data, timeout=30, headers={'Content-Type': 'application/json; charset=utf-8'})
    result = resp.json()
    
    if result.get('errcode', 0) == 0:
        media_id = result.get('media_id')
        print(f"\n✅ 发布成功！")
        print(f"   草稿 ID: {media_id}")
        print(f"   请前往公众号后台查看：https://mp.weixin.qq.com")
        return media_id
    else:
        err_msg = result.get('errmsg', '未知错误')
        err_code = result.get('errcode', 0)
        print(f"\n❌ 发布失败：{err_msg}")
        print(f"   错误码：{err_code}")
        raise Exception(f"发布失败：{err_msg}")

def main():
    print("=" * 60)
    print("微信公众号文章发布工具（Knowledge-Base 主题版）")
    print("作者：黑白交织")
    print("=" * 60)
    print()
    
    # 1. 上传封面图
    print("📷 步骤 1: 上传封面图...")
    image_path = '/home/admin/Downloads/openclaw.png'
    print(f"   图片路径：{image_path}")
    thumb_media_id = upload_cover_image(image_path)
    
    if not thumb_media_id:
        print("\n❌ 封面图上传失败")
        sys.exit(1)
    
    print()
    
    # 2. 创建文章内容
    print("📝 步骤 2: 创建文章内容（Knowledge-Base 风格）...")
    content = create_wechat_article_kb_style()
    print(f"   内容长度：{len(content)}")
    print()
    
    # 3. 发布
    print("🚀 步骤 3: 发布到草稿箱...")
    try:
        create_draft(
            title='工作看板管理实战',
            content=content,
            summary='300 秒→5 秒，效率提升 57 倍',
            thumb_media_id=thumb_media_id
        )
    except Exception as e:
        print(f"\n❌ 发布失败：{e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
