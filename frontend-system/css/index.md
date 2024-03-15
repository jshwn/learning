# CSS

CSS documentation index: https://developer.mozilla.org/en-US/docs/Web/CSS

##  Domain
* meta logical
  * scope: `@scope`, `:scope`, `:root`
  * logical: `:nth-of-type()`, `:fullscreen`
  * pip mode: `:picture-in-picture`
* layout
  * grid, flex, column
  * page
    * `@page`, `:left`, `:right`
  * considering text content size
    * 참고: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_text/Wrapping_breaking_text
    * `<wbr />`
* text, font
  * `::first-letter`, 
* color
* image
* link, url, target
  * `:link`, `:visited`, `:local-link`, `:target`, `:any-link`
* input, select, option, textarea, form
  * validation: `:required`, `:optional`, `:valid`, `:invalid`, `:user-valid`, `:user-invalid`
  * placeholder: `:placeholder-shown`
  * `:default`, `:autofill`, `:indeterminate`, `:in-range`, `:out-of-range`, `:read-only`, `:read-write`, `:checked`, `:enabled`,
  * `::file-selector-button`
  * __여담: input 쪽 도메인은 pseudo element보다는 attribute selector(input\[type=""\])을 쓰는 게 더 쉽고 통일성이 높을 것 같다__
* interaction
  * focus: `:focus`, `:focus-visible`, `:focus-within`
  * dialog: `:modal`, `::backdrop`
  * hover: `:hover`
  * popover: `:popover-open`, `::backdrop`
  * selection: `::selection` (user drag)
  * scroll: `scroll-snap-type`, `scroll-snap-align`, `scroll-padding`, `scroll-margin`, `scroll-snap-stop`
    * 참고: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap/Basic_concepts
* video, WebVTT, audio, ...
  * `:current`, `:seeking`, `:stalled`, `:muted`, `:playing`, `:paused`, `:past`, `:future`, `:volume-lockd`
  * WebVTT specific: `::cue`, `::cue-region`
