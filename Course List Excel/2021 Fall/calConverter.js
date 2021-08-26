const fs = require("fs");
const csv = fs.readFileSync("fallCalCsv.csv");

const array = csv.toString().split("\r\n");
const result = [];
const header = array[0].split(",");

for (const ele of header) {
  ele.trim();
}

for (let i = 1; i < array.length; i++) {
  const obj = {};
  const toFill = array[i].split(",");

  for (const ele of toFill) {
    ele.trim();
  }
  for (let j = 0; j < toFill.length; j++) {
    if (header[j] === "holiday") {
      switch (toFill[j]) {
        case "FALSE":
          obj[header[j]] = false;
          break;
        default:
          obj[header[j]] = true;
          break;
      }
    } else if (header[j] === "date") {
      obj[header[j]] = toFill[j];
    } else if (header[j] === "title") {
      obj[header[j]] = [toFill[j]];
    } else if (header[j] === "contents") {
      obj[header[j]] = [toFill[j]];
    }
  }
  result.push(obj);
}
const json = JSON.stringify(result);
fs.writeFileSync("calendar.json", json);
