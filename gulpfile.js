const sass = require("gulp-sass")(require("sass"));
const { series, src, dest } = require("gulp");
const del = require("del");
const gpug = require("gulp-pug");
let src_path = "./src/";
let dist = "./dist/";
let PATHS = {
  pug: `${src_path}/pug/*.pug`,
  scss: `${src_path}/scss/*.scss`,
  img: `${src_path}/img/*.*`,
  clean: `${dist}`,
};
function clear() {
  return del(dist);
}
function buildStyles() {
  return src(PATHS["scss"])
    .pipe(sass().on("error", sass.logError))
    .pipe(dest(dist));
}
function image() {
  return src(PATHS["img"]).pipe(dest(dist));
}
function compilePug() {
  return src(PATHS["pug"]).pipe(gpug()).pipe(dest(dist));
}
function defaultTask() {
  return series(compilePug);
}
exports.default = series(clear,buildStyles, image, compilePug);
exports.clear = clear;
