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

🛠️ **Kullanılabilir Araçlar (MCP Tools)**

Bu FastMCP sunucusu LLM modelleri için **6 araç** sunar.

### Marka Araçları

#### **`search_trademarks`** — Marka Arama
Türkiye'de tescilli markaları arar.
* `trademark_name`: Marka adı
* `name_operator`: Arama operatörü — `contains` (içinde geçen, varsayılan), `startsWith` (ile başlayan), `equals` (eşit)
* `holder_name`: Marka sahibi/başvuru sahibi adı
* `holder_name_operator`: Sahip adı arama operatörü — `startsWith` (varsayılan), `equals`
* `nice_classes`: Nice sınıflandırma kodları, virgülle ayrılmış (örn. `"9,35,42"`)
* `limit`: Sayfa başına sonuç sayısı (varsayılan: 20, maks: 100)
* `offset`: Sayfalama ofseti

#### **`get_trademark_details`** — Marka Detayı
Belirli bir marka başvurusunun detaylı bilgilerini getirir.
* `application_number`: Marka başvuru numarası (örn. `"T/01853"`, `"2020/12345"`)

**Dönen bilgiler:** Marka adı, sahibi, Nice sınıfları, başvuru tarihi, tescil durumu, bülten numaraları, koruma tarihleri.

### Patent Araçları

#### **`search_patents`** — Patent Arama
Türkiye'de tescilli patentleri arar.
* `title`: Buluş başlığı
* `abstract`: Buluş özeti anahtar kelimeleri
* `owner`: Buluş sahibi (mucit) adı
* `applicant`: Başvuru sahibi adı
* `application_number`: Patent başvuru numarası
* `ipc_class`: IPC sınıflandırma kodu (örn. `"G06F"`, `"H01Q"`)
* `cpc_class`: CPC sınıflandırma kodu
* `attorney`: Patent vekili adı
* `limit`: Sayfa başına sonuç sayısı (varsayılan: 20, maks: 100)
* `offset`: Sayfalama ofseti

#### **`get_patent_details`** — Patent Detayı
Belirli bir patent başvurusunun detaylı bilgilerini getirir.
* `application_number`: Patent başvuru numarası

**Dönen bilgiler:** Başlık, özet, buluş sahipleri, başvuru sahibi, IPC/CPC sınıfları, rüçhan bilgileri, yayın tarihleri, vekil bilgisi, işlem geçmişi.

### Tasarım Araçları

#### **`search_designs`** — Endüstriyel Tasarım Arama
Türkiye'de tescilli endüstriyel tasarımları arar.
* `design_name`: Tasarım adı
* `designer`: Tasarımcı adı
* `applicant`: Başvuru sahibi adı
* `registration_no`: Tasarım tescil numarası
* `locarno_class`: Locarno sınıflandırma kodu (örn. `"06-01"`)
* `attorney`: Tasarım vekili adı
* `limit`: Sayfa başına sonuç sayısı (varsayılan: 20, maks: 100)
* `offset`: Sayfalama ofseti

#### **`get_design_details`** — Tasarım Detayı
Belirli bir tasarım başvurusunun detaylı bilgilerini getirir.
* `file_id`: Tasarım dosya ID'si (`search_designs` sonuçlarından alınır)

**Dönen bilgiler:** Tasarım adı, tasarımcı, başvuru sahibi, Locarno sınıfı, tescil detayları, bülten tarihleri, işlem geçmişi.

---
📜 **Lisans**

Bu proje MIT Lisansı altında lisanslanmıştır.
