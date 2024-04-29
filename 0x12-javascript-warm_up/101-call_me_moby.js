#!/usr/bin/node
/* change myVar to 333 */
exports.callMeMoby = function (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
