#!/usr/bin/node
/* change increment x by 1 */
let nb;
exports.addMeMaybe = function (x, func) {
  func(nb = x + 1);
  return nb;
};
