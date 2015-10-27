/*!
 * IE10 viewport hack for Surface/desktop Windows 8 bug
<<<<<<< HEAD
 * Copyright 2014-2015 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
=======
 * Copyright 2014 Twitter, Inc.
 * Licensed under the Creative Commons Attribution 3.0 Unported License. For
 * details, see http://creativecommons.org/licenses/by/3.0/.
>>>>>>> 69c299e4da22fca281499a293237320536e9cfa0
 */

// See the Getting Started docs for more information:
// http://getbootstrap.com/getting-started/#support-ie10-width

(function () {
  'use strict';
<<<<<<< HEAD

=======
>>>>>>> 69c299e4da22fca281499a293237320536e9cfa0
  if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
    var msViewportStyle = document.createElement('style')
    msViewportStyle.appendChild(
      document.createTextNode(
        '@-ms-viewport{width:auto!important}'
      )
    )
    document.querySelector('head').appendChild(msViewportStyle)
  }
<<<<<<< HEAD

=======
>>>>>>> 69c299e4da22fca281499a293237320536e9cfa0
})();
