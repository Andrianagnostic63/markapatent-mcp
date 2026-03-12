# Marka Patent MCP: TÜRKPATENT Marka, Patent ve Tasarım Araştırma MCP Sunucusu

Bu proje, Türk Patent ve Marka Kurumu'na ait araştırma portalına (`turkpatent.gov.tr`) erişimi kolaylaştıran bir [FastMCP](https://gofastmcp.com/) sunucusu oluşturur. Bu sayede, TÜRKPATENT veritabanında marka, patent ve endüstriyel tasarım araması yapma işlemleri, Model Context Protocol (MCP) destekleyen LLM uygulamaları (örneğin Claude Desktop veya [5ire](https://5ire.app)) ve diğer istemciler tarafından araç (tool) olarak kullanılabilir hale gelir.

🎯 **Temel Özellikler**

* TÜRKPATENT araştırma portalına programatik erişim için standart bir MCP arayüzü.
* **6 araç** ile kapsamlı fikri mülkiyet araştırması:
    * **Marka** — Ada, sahibe, Nice sınıfına göre arama ve detay
    * **Patent** — Başlık, özet, buluş sahibi, başvuru sahibi, IPC/CPC sınıfına göre arama ve detay
    * **Endüstriyel Tasarım** — Ada, tasarımcıya, başvuru sahibine, Locarno sınıfına göre arama ve detay
* Gelişmiş özellikler:
    * Tüm arama araçlarında sayfalama (limit/offset) desteği
    * In-memory caching (arama: 10 dk, detay: 1 saat)
    * Arama operatörleri: içinde geçen, ile başlayan, eşit (marka aramasında)

---

## 🚀 Kurulum Gerektirmez! Hemen Kullan!

🔗 **Remote MCP Adresi:** `https://markapatent-mcp.fastmcp.app/mcp`

### Claude Desktop ile Kullanım

1. **Claude Desktop'ı açın**
2. **Settings → Connectors → Add Custom Connector**
3. **Bilgileri girin:**
   - **Name:** `Marka Patent MCP`
   - **URL:** `https://markapatent-mcp.fastmcp.app/mcp`
4. **Save** butonuna tıklayın
5. **Hemen kullanmaya başlayın!** 🎉

### Google Antigravity ile Kullanım

1. **Agent session** açın ve editörün yan panelindeki **"…"** dropdown menüsüne tıklayın
2. **MCP Servers** seçeneğini seçin - MCP Store açılacak
3. Üstteki **Manage MCP Servers** butonuna tıklayın
4. **View raw config** seçeneğine tıklayın
5. `mcp_config.json` dosyasına aşağıdaki yapılandırmayı ekleyin:

```json
{
  "mcpServers": {
    "markapatent-mcp": {
      "serverUrl": "https://markapatent-mcp.fastmcp.app/mcp/",
      "headers": {
        "Content-Type": "application/json"
      }
    }
  }
}
```

> 💡 **İpucu:** Remote MCP sayesinde Python, uv veya herhangi bir kurulum yapmadan doğrudan TÜRKPATENT veritabanına erişebilirsiniz!

---
📜 **Lisans**

Bu proje MIT Lisansı altında lisanslanmıştır.
