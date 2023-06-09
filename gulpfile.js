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
// npm i gulp-svgmin
// npm i gulp-htmlmin

import dartSass from "sass";
import gulpSass from "gulp-sass";
const sass = gulpSass(dartSass);
import gulp from "gulp";
import del from "del";
import gpug from "gulp-pug";
import gimagemin from "gulp-imagemin";
import gwebp from "imagemin-webp";
import rename from "gulp-rename";
import svgmin from "gulp-svgmin";
import htmlmin from "gulp-htmlmin";

const PATHS = {
  src: "src",
  dist: "dist",
  clean: "dist",
};
const FILES = {
  pug: [`${PATHS["src"]}/**/*.pug`, `!${PATHS["src"]}/**/_*.pug`],
  scss: `${PATHS["src"]}/scss/*.scss`,
  img: `${PATHS["src"]}/**/*.{png,jpg}`,
  js: `${PATHS["src"]}/**/*.js`,
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
    .pipe(gimagemin([gwebp({ quality: 40 })]))
    .pipe(rename({ extname: ".webp" }))
    .pipe(gulp.dest(PATHS["dist"]));
}
function svg() {
  return (
    gulp
      .src(FILES["svg"])
      // .pipe(
      //   svgmin({
      //     multipass: true,
      //     plugins: [
      //       {
      //         name: "cleanupIDs",
      //         active: false,
      //       },
      //     ],
      //   })
      // )
      .pipe(gulp.dest(PATHS["dist"]))
  );
}
function compilePug() {
  return (
    gulp
      .src(FILES["pug"])
      .pipe(gpug())
      // // .pipe(
      // //   htmlmin({
      // //     collapseWhitespace: true,
      // //     removeComments: true,
      // //   })
      // )
      .pipe(gulp.dest(PATHS["dist"]))
  );
}
function scripts() {
  return gulp.src(FILES["js"]).pipe(gulp.dest(PATHS["dist"]));
}
function watch() {
  gulp.watch(FILES["scss"], buildStyles);
  gulp.watch(FILES["pug"][0], compilePug);
  gulp.watch(FILES["js"], scripts);
  // watch(PATHS.pug,compilePug)
}
gulp.task("image", image);
gulp.task("svg", svg);
gulp.task("graphics", () => {
  return gulp.parallel(image, svg);
});
gulp.task(
  "build",
  gulp.series(
    clear,
    gulp.parallel(buildStyles, image, svg, compilePug, scripts),
    watch
  )
);
export default gulp.series(clear, buildStyles, image, svg, compilePug, scripts);
export { clear };
export { watch };
