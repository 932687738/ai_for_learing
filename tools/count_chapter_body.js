const fs = require('fs')
const path = process.argv[2]
if (!path) {
  console.error('Usage: node count_chapter_body.js <file>')
  process.exit(1)
}
const content = fs.readFileSync(path, 'utf8')
const body = content.split('## 本章状态更新')[0]
const noWs = body.replace(/\s/g, '')
console.log(noWs.length)
