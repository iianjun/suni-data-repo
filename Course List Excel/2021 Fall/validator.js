const fs = require("fs");
const json = fs.readFileSync("all.json");
const courses = JSON.parse(json);
const stringFieldValidator = (name) => {
  return !name.includes('"') && !name.includes(`/`) && !name.includes(`\\`);
};
const majorValidator = (major) => {
  return (
    major === "TSM" ||
    major === "CSE" ||
    major === "MEC" ||
    major === "AMS" ||
    major === "BUS" ||
    major === "ETC"
  );
};
for (const course of courses) {
  //name field
  if (typeof course["name"] !== "string") {
    console.log(course);
    console.log("Error: name field is not a string");
    break;
  }
  if (!stringFieldValidator(course["name"])) {
    console.log(course);
    console.log("Error: name field contains defect character");
    break;
  }
  if (!stringFieldValidator(course["title"])) {
    console.log(course);
    console.log("Error: title field contains defect character");
    break;
  }

  if (typeof course["hasLab"] !== "boolean") {
    console.log(course);
    console.log("Error: hasLab field contains not boolean value");
    break;
  }
  if (typeof course["credit"] !== "number") {
    if (isNan(course["credit"])) {
      console.log(course);
      console.log("Error: credit field is Nan Value");
    }
    console.log(course);
    console.log("Error: credit field contains not number value");
    break;
  }
  if (course["number"] && typeof course["number"] !== "number") {
    if (isNan(course["number"])) {
      console.log(course);
      console.log("Error: number field is Nan Value");
    }
    console.log(course);
    console.log("Error: number field contains not number value");
    break;
  }

  if (typeof course["days"] !== "object") {
    console.log(course);
    console.log("Error: type of days is not an array");
    break;
  }
  if (!majorValidator(course["major"])) {
    console.log(course);
    console.log("Error: Unknown Major");
    break;
  }
}
