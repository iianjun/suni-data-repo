const fs = require("fs");
const csv = fs.readFileSync("Others.csv");

const array = csv.toString().split("\r\n");
const result = [];
const header = array[0].split(",");

//in case there is a space
for (const ele of header) {
  ele.trim();
}
for (let i = 1; i < array.length - 1; i++) {
  const obj = {};
  const toFill = array[i].split(",");

  //in case there is a space
  for (const ele of toFill) {
    ele.trim();
  }
  for (let j = 0; j < toFill.length; j++) {
    if (header[j] === "days") {
      switch (toFill[j]) {
        case "M":
          obj[header[j]] = ["MON"];
          break;
        case "MW":
          obj[header[j]] = ["MON", "WED"];
          break;
        case "RECM":
          obj[header[j]] = ["MON"];
          break;
        case "TUTH":
          obj[header[j]] = ["TUE", "THU"];
          break;
        case "RECF":
          obj[header[j]] = ["FRI"];
          break;
        case "TH":
          obj[header[j]] = ["THU"];
          break;
        case "W":
          obj[header[j]] = ["WED"];
          break;
        case "TU":
          obj[header[j]] = ["TUE"];
          break;
        case "RECW":
          obj[header[j]] = ["WED"];
          break;
        case "MF":
          obj[header[j]] = ["MON", "FRI"];
          break;
        case "F":
          obj[header[j]] = ["FRI"];
          break;
        case "RETU":
          obj[header[j]] = ["TUE"];
          break;
        case "RETH":
          obj[header[j]] = ["THU"];
          break;
      }
    } else if (header[j] === "hasLab") {
      obj[header[j]] = toFill[j] === "FALSE" ? false : true;
    } else if (header[j] === "number") {
      if (toFill[j] !== "") {
        obj[header[j]] = parseInt(toFill[j]);
      }
    } else if (header[j] === "credit") {
      obj[header[j]] = parseInt(toFill[j]);
    } else {
      obj[header[j]] = toFill[j];
    }
  }

  //   break;
  result.push(obj);
}
const json = JSON.stringify(result);
fs.writeFileSync("Others.json", json);
