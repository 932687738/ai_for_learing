const fs = require('fs')
const path = require('path')
const dir = path.join(__dirname, '..', 'story', '人皮契约', '正文')
const files = ['023', '024', '025', '026', '027', '028']
const glob = fs.readdirSync(dir)
for (const num of files) {
  const f = glob.find((x) => x.startsWith(`第${num}章`))
  if (!f) {
    console.log(`${num}: NOT FOUND`)
    continue
  }
  const content = fs.readFileSync(path.join(dir, f), 'utf8')
  const body = content.split('## 本章状态更新')[0]
  const noWs = body.replace(/\s/g, '')
  console.log(`${num}:${noWs.length}`)
}
