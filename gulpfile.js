// npm i concurrently
// npm i del
// npm i gulp
// npm i gulp-pug
// npm i pug
// npm i pug-cli
// npm i gulp-sass
// npm i sass
// npm i imagemin-webp
// npm i gulp-webp
// npm i gulp-ext-replace
// npm i gulp-imagemin
// npm i gulp-rename

import dartSass from "sass";
import gulpSass from "gulp-sass";
const sass = gulpSass(dartSass);
import gulp from "gulp";
import del from "del";
import gpug from "gulp-pug";
import gimagemin from "gulp-imagemin";
import gwebp from "imagemin-webp";
import rename from "gulp-rename";
// const pwd =
//   "/Users/ivantolmacev/Library/Mobile Documents/com~apple~CloudDocs/Documents/University/";
const PATHS = {
  src: "src",
  dist: "dist",
  clean: "dist",
};
const FILES = {
  pug: `${PATHS["src"]}/**/*.pug`,
  scss: `${PATHS["src"]}/scss/*.scss`,
  img: `${PATHS["src"]}/**/*.{png,jpg}`,
  svg: `${PATHS["src"]}/**/*.svg`,
};
function clear() {
  return del(PATHS["dist"]);
}
function buildStyles() {
  return gulp
    .src(FILES["scss"])
    .pipe(sass().on("error", sass.logError))
    .pipe(gulp.dest(PATHS["dist"]));
}
function image() {
  return gulp
    .src(FILES["img"])
    .pipe(gimagemin([gwebp({ quality: 50 })]))
    .pipe(rename({ extname: ".webp" }))
    .pipe(gulp.dest(PATHS["dist"]));
}
function svg() {
  return gulp.src(FILES["svg"]).pipe(gulp.dest(PATHS["dist"]));
}
function compilePug() {
  return gulp.src(FILES["pug"]).pipe(gpug()).pipe(gulp.dest(PATHS["dist"]));
}
function watch() {
  watch(FILES["scss"], buildStyles);
  watch(FILES["pug"], compilePug);
  // watch(PATHS.pug,compilePug)
}
gulp.task("image", image);
gulp.task("svg", svg);
gulp.task("graphics", () => {
  return gulp.parallel(image, svg);
});
export default gulp.series(clear, buildStyles, image, svg, compilePug);
export { clear };
export { watch };
