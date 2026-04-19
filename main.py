# Source Generated with Decompyle++
# File: main.cpython-310.pyc (Python 3.10)

import json
import urllib.request as urllib
from urllib.parse import quote
from pathlib import Path
from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse
PLUGIN_DIR = Path(__file__).parent
CONFIG_FILE = PLUGIN_DIR / 'config.json'

def _load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r', 'utf-8', **('encoding',)) as f:
            None(None, None, None)
            return json.load(f)
            with None:
                if not None:
                    pass
    return {
        'city': '天津',
        'qweather_key': '',
        'provider': 'wttr' }


def _save_config(cfg):
    with open(CONFIG_FILE, 'w', 'utf-8', **('encoding',)) as f:
        json.dump(cfg, f, False, 2, **('ensure_ascii', 'indent'))
        None(None, None, None)
        return None
        with None:
            if not None:
                pass


def _fetch_wttr(city):
    url = f'''https://wttr.in/{quote(city)}?format=j1&lang=zh'''
    req = urllib.request.Request(url, {
        'User-Agent': 'curl/7.68.0' }, **('headers',))
    with urllib.request.urlopen(req, 10, **('timeout',)) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        cur = data.get('current_condition', [
            { }])[0]
        today = data.get('weather', [
            { }])[0]
        None(None, None, None)
        return {
            'city': city,
            'temp_C': cur.get('temp_C'),
            'feels_like': cur.get('FeelsLikeC'),
            'humidity': cur.get('humidity'),
            'desc': cur.get('lang_zh', [
                { }])[0].get('value', cur.get('weatherDesc', [
                { }])[0].get('value', '')),
            'wind_kmh': cur.get('windspeedKmph'),
            'min_temp': today.get('mintempC'),
            'max_temp': today.get('maxtempC') }
        with None:
            if not None:
                pass


def _fetch_qweather(city, key):
    loc_url = f'''https://geoapi.qweather.com/v2/city/lookup?location={quote(city)}&key={key}'''
    req = urllib.request.Request(loc_url)
    with urllib.request.urlopen(req, 10, **('timeout',)) as resp:
        loc_data = json.loads(resp.read().decode('utf-8'))
        if not loc_data.get('code') != '200' or loc_data.get('location'):
            raise Exception(f'''城市查询失败: code={loc_data.get('code')}''')
        location_id = loc_data['location'][0]['id']
        None(None, None, None)
    with None:
        if not None:
            pass
    weather_url = f'''https://devapi.qweather.com/v7/weather/now?location={location_id}&key={key}'''
    req2 = urllib.request.Request(weather_url)
    with urllib.request.urlopen(req2, 10, **('timeout',)) as resp:
        w = json.loads(resp.read().decode('utf-8'))
        if w.get('code') != '200':
            raise Exception(f'''天气查询失败: code={w.get('code')}''')
        now = w.get('now', { })
        None(None, None, None)
        return {
            'city': city,
            'temp_C': now.get('temp'),
            'feels_like': now.get('feelsLike'),
            'humidity': now.get('humidity'),
            'desc': now.get('text', ''),
            'wind_kmh': now.get('windSpeed'),
            'min_temp': None,
            'max_temp': None }
        with None:
            if not None:
                pass


def _fetch_weather(city = (None,)):
    cfg = _load_config()
    if not city:
        pass
    city = cfg.get('city', '天津')
    key = cfg.get('qweather_key', '')
    provider = cfg.get('provider', 'wttr')
    if provider == 'qweather' and key:
        return _fetch_qweather(city, key)
    return None(city)


def register(app, mcp_server = (None,)):
    
    async def weather_api(city = None):
        pass
    # WARNING: Decompyle incomplete

    weather_api = None(weather_api)
    
    async def weather_settings_page():
        cfg = _load_config()
        html = SETTINGS_HTML
        html = html.replace('%%CITY%%', cfg.get('city', '天津'))
        html = html.replace('%%KEY%%', cfg.get('qweather_key', ''))
        html = html.replace('%%PROVIDER%%', cfg.get('provider', 'wttr'))
        return html

    weather_settings_page = app.get('/weather/settings', HTMLResponse, **('response_class',))(weather_settings_page)
    
    async def save_weather_settings(request = None):
        await request.json()
        body = <NODE:28>
        cfg = _load_config()
        cfg['city'] = body.get('city', cfg.get('city', '天津')).strip()
        cfg['qweather_key'] = body.get('qweather_key', '').strip()
        cfg['provider'] = body.get('provider', 'wttr')
        _save_config(cfg)
        return {
            'status': 'success',
            'message': '设置已保存，立即生效' }

    save_weather_settings = None(save_weather_settings)
    if mcp_server:
        
        async def mcp_weather(city = None):
            '''查询指定城市实时天气。
            city: 城市名（可选，不传则使用默认城市）。
            返回：温度、体感温度、湿度、天气描述、今日温度范围。
            '''
            pass
        # WARNING: Decompyle incomplete

        mcp_weather = None(mcp_weather)
        return None

SETTINGS_HTML = '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>🌤️ 天气插件设置</title>\n<style>\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:linear-gradient(135deg,#A0D8EF 0%,#7CC2DE 100%);min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}\n.card{background:#fff;border-radius:16px;padding:30px;width:100%;max-width:460px;box-shadow:0 10px 40px rgba(0,0,0,.15)}\n.card h2{color:#333;margin-bottom:6px;font-size:1.5em}\n.sub{color:#999;font-size:13px;margin-bottom:24px}\nlabel{display:block;font-size:14px;color:#555;font-weight:600;margin-bottom:6px}\ninput,select{width:100%;padding:10px 14px;border:2px solid #e0e0e0;border-radius:10px;font-size:14px;margin-bottom:18px;transition:border .3s}\ninput:focus,select:focus{outline:none;border-color:#A0D8EF}\n.hint{font-size:12px;color:#aaa;margin-top:-14px;margin-bottom:18px}\nbutton{width:100%;padding:12px;border:none;border-radius:10px;font-size:16px;font-weight:600;cursor:pointer;transition:all .2s}\n.btn-p{background:linear-gradient(135deg,#A0D8EF,#7CC2DE);color:#fff;margin-bottom:10px}\n.btn-p:hover{transform:translateY(-2px);box-shadow:0 5px 15px rgba(160,216,239,.4)}\n.btn-t{background:#f0f9ff;color:#555;border:1px solid #A0D8EF;margin-bottom:10px}\n.btn-b{background:#f5f5f5;color:#888}\n.msg{padding:10px;border-radius:8px;margin-bottom:14px;font-size:14px;display:none}\n.msg.ok{display:block;background:#d4edda;color:#155724}\n.msg.err{display:block;background:#f8d7da;color:#721c24}\n.test-r{background:#f8f9fa;border-radius:10px;padding:14px;margin-bottom:14px;font-size:14px;display:none;line-height:1.6}\n#keyField{display:none}\n</style>\n</head>\n<body>\n<div class="card">\n<h2>🌤️ 天气插件设置</h2>\n<p class="sub">配置默认城市和天气数据源 · 保存即生效</p>\n<div id="msg" class="msg"></div>\n<label>默认城市</label>\n<input type="text" id="city" value="%%CITY%%" placeholder="如：北京、上海、天津">\n<label>数据源</label>\n<select id="provider" onchange="tog()">\n<option value="wttr">wttr.in（免费，无需 Key）</option>\n<option value="qweather">和风天气（需 API Key）</option>\n</select>\n<div id="keyField">\n<label>和风天气 API Key</label>\n<input type="text" id="qkey" value="%%KEY%%" placeholder="填入你的 Key">\n<p class="hint">在 <a href="https://console.qweather.com" target="_blank">console.qweather.com</a> 免费申请</p>\n</div>\n<div id="testR" class="test-r"></div>\n<button class="btn-t" onclick="test()">🧪 测试一下</button>\n<button class="btn-p" onclick="save()">💾 保存设置</button>\n<button class="btn-b" onclick="location.href=\'/\'">← 返回主页</button>\n</div>\n<script>\nfunction tog(){document.getElementById(\'keyField\').style.display=document.getElementById(\'provider\').value===\'qweather\'?\'block\':\'none\'}\n(function(){document.getElementById(\'provider\').value=\'%%PROVIDER%%\';tog()})();\nasync function save(){\n  try{\n    var r=await fetch(\'/weather/settings\',{method:\'POST\',headers:{\'Content-Type\':\'application/json\'},body:JSON.stringify({city:document.getElementById(\'city\').value,provider:document.getElementById(\'provider\').value,qweather_key:document.getElementById(\'qkey\').value})});\n    var d=await r.json();sm(\'ok\',\'✅ \'+d.message)\n  }catch(e){sm(\'err\',\'❌ \'+e.message)}\n}\nasync function test(){\n  var c=document.getElementById(\'city\').value.trim()||\'北京\',el=document.getElementById(\'testR\');\n  el.style.display=\'block\';el.textContent=\'🔍 查询中...\';\n  try{\n    var r=await fetch(\'/api/weather?city=\'+encodeURIComponent(c)),d=await r.json();\n    if(d.error){el.innerHTML=\'❌ \'+d.error;return}\n    el.innerHTML=\'🌡️ <b>\'+d.city+\'</b>: \'+(d.desc||\'\')+\' \'+d.temp_C+\'°C\'+(d.feels_like?\' (体感\'+d.feels_like+\'°C)\':\'\')+\' | 湿度\'+(d.humidity||\'?\')+\'%\'+(d.min_temp?\' | 今日\'+d.min_temp+\'~\'+d.max_temp+\'°C\':\'\')\n  }catch(e){el.innerHTML=\'❌ \'+e.message}\n}\nfunction sm(t,s){var e=document.getElementById(\'msg\');e.className=\'msg \'+(t===\'ok\'?\'ok\':\'err\');e.textContent=s;setTimeout(function(){e.style.display=\'none\'},3000)}\n</script>\n</body>\n</html>'
