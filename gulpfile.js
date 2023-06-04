const sass = require("gulp-sass")(require("sass"));
const { series, src, dest, watch } = require("gulp");
const del = require("del");
const gpug = require("gulp-pug");
// const pwd =
//   "/Users/ivantolmacev/Library/Mobile Documents/com~apple~CloudDocs/Documents/University/";
const PATHS = {
  src: "src",
  dist: "dist",
  clean: "dist",
};
const FILES = {
  pug: `${PATHS["src"]}/pug/*.pug`,
  scss: `${PATHS["src"]}/scss/*.scss`,
  img: `${PATHS["src"]}/img/*.*`,
};
function clear() {
  return del(PATHS["dist"]);
}
function buildStyles() {
  return src(FILES["scss"])
    .pipe(sass().on("error", sass.logError))
    .pipe(dest(PATHS["dist"]));
}
function image() {
  return src(FILES["img"]).pipe(dest(PATHS["dist"]));
}
function compilePug() {
  return src(FILES["pug"]).pipe(gpug()).pipe(dest(PATHS["dist"]));
}
exports.default = series(clear, buildStyles, image, compilePug);
exports.clear = clear;
exports.watch = function () {
  watch(FILES["scss"], buildStyles);
  watch(FILES["pug"], compilePug);
  // watch(PATHS.pug,compilePug)
};
