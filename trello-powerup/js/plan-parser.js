/*
 * plan-parser.js — turn a GTM plan (Markdown) into structured phases.
 *
 * Pure, dependency-free, and browser/Node safe so it can be unit-tested.
 * Recognizes the intern plan format:
 *   # … — Intern GTM Plan            -> planTitle
 *   **Region:** …                    -> meta.Region (also Vertical focus/Goal/Objectives)
 *   ## Phase 1 — Product immersion…   -> a phase (name = full heading text)
 *   *Outcome: …*                      -> phase.outcome
 *   - do the thing                    -> phase.tasks[]
 * Any other `## Heading` ends the current phase capture.
 */
(function (root) {
  function cleanInline(s) {
    return String(s)
      .replace(/\*\*(.+?)\*\*/g, '$1')          // bold
      .replace(/(^|[^*])\*(?!\s)(.+?)\*/g, '$1$2') // italics
      .replace(/`([^`]+)`/g, '$1')              // inline code
      .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')  // [text](url) -> text
      .replace(/\s+/g, ' ')
      .trim();
  }

  function parsePlan(md) {
    var lines = String(md == null ? '' : md).replace(/\r\n/g, '\n').split('\n');
    var planTitle = '';
    var meta = {};
    var phases = [];
    var current = null;

    var h1Re = /^#\s+(.+?)\s*$/;
    var h2Re = /^##\s+/;
    var phaseRe = /^##\s+Phase\s+(\d+)\s*[—\-:]\s*(.+?)\s*$/i;
    var metaRe = /^\*\*(Region|Vertical focus|Goal|Objectives):\*\*\s*(.+?)\s*$/i;
    var outcomeRe = /^\*\s*Outcome:\s*(.+?)\s*\*$/i;
    var bulletRe = /^[-*]\s+(.+?)\s*$/;

    for (var i = 0; i < lines.length; i++) {
      var line = lines[i].replace(/\s+$/, '');

      var h1 = line.match(h1Re);
      if (h1 && !h2Re.test(line) && !planTitle) { planTitle = cleanInline(h1[1]); continue; }

      var ph = line.match(phaseRe);
      if (ph) {
        current = {
          number: Number(ph[1]),
          title: cleanInline(ph[2]),
          name: 'Phase ' + ph[1] + ' — ' + cleanInline(ph[2]),
          outcome: '',
          tasks: []
        };
        phases.push(current);
        continue;
      }

      if (h2Re.test(line)) { current = null; continue; } // some other section

      if (!current) {
        var m = line.match(metaRe);
        if (m) { meta[m[1].replace(/\s+/g, '_')] = cleanInline(m[2]); }
        continue;
      }

      var oc = line.match(outcomeRe);
      if (oc) { current.outcome = cleanInline(oc[1]); continue; }

      var b = line.match(bulletRe);
      if (b) {
        var task = cleanInline(b[1]);
        if (task) current.tasks.push(task);
      }
    }

    return { planTitle: planTitle, meta: meta, phases: phases };
  }

  root.parsePlan = parsePlan;
  if (typeof module !== 'undefined' && module.exports) { module.exports = { parsePlan: parsePlan, cleanInline: cleanInline }; }
})(typeof window !== 'undefined' ? window : this);
