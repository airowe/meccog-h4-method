"""Build H4_submission.xlsx from the official template and rows/<PMID>.json.

The template is copied, never edited in place. ORDER below lists the papers;
main() ranks them by relevance (rules: "P1 holding the findings most relevant
to the hypothesis"): highest finding relevance first, then mean relevance,
then ORDER position. Findings keep the order of each JSON file.
"""
import json, os, shutil, sys
import openpyxl

BASE = os.path.expanduser('~/Documents/Alzheimers')
WORK = os.path.join(BASE, 'H4_work')
TEMPLATE = os.path.join(WORK, 'resources', 'submission_template.xlsx')
OUT = os.path.join(BASE, 'H4_submission.xlsx')

HYPOTHESIS = ("In some types of non-Alzheimer's, non-aged human brain cells, APOE4 adheres more tightly "
              "to some recycling receptors than APOE3, impeding recycling.")
# Keys are rows/<key>.json names: the PMID, or a slug for a source with no PMID.
ORDER = ['30375977', '28957663', '28276521', '20547867', '34617884', '38217595', '29946028', '31796678', '34982109', '32588544', '34557909', '39532095', '43026723', '16540478', '15863833', '15485881', '9593678', '17079794', '18369154', '10070023', '11369796', '37060729', '8808766', '12969990', '12950167', '18359298', '38279679', '8632164', '25482438']
STRENGTH = {1: '1 very strong', 2: '2 strong', 3: '3 moderate', 4: '4 weak', 5: '5 very weak'}
# Method-sheet values live in an untracked local file (contains contact details).
METHOD = json.load(open(os.path.join(WORK, 'method.local.json')))


def load(key):
    rows = json.load(open(os.path.join(WORK, 'rows', f'{key}.json')))
    return [x for x in rows[1:] if not x.get('paper')]


def rank(keys, findings_of):
    def score(key):
        rels = [float(f['relevance']) for f in findings_of(key)]
        return (-max(rels), -sum(rels) / len(rels))
    return sorted(keys, key=score)


def main(order=ORDER):
    order = rank(order, load)
    shutil.copyfile(TEMPLATE, OUT)
    wb = openpyxl.load_workbook(OUT)
    ws = wb['Submission']
    ws['A2'] = HYPOTHESIS
    r = 3
    counts = {'papers': 0, 'findings': 0, 'against': 0}
    for pi, key in enumerate(order, 1):
        rows = json.load(open(os.path.join(WORK, 'rows', f'{key}.json')))
        paper, findings = rows[0], [x for x in rows[1:] if not x.get('paper')]
        assert paper.get('paper') and str(paper.get('key', paper['pmid'])) == key, key
        ws.cell(r, 2, paper['doi']); ws.cell(r, 3, paper['source_type'])
        ws.cell(r, 4, str(paper['pmid'])); ws.cell(r, 5, f'P{pi}')
        r += 1
        counts['papers'] += 1
        for fi, f in enumerate(findings, 1):
            vals = [f'P{pi}.F{fi}', f['description'], f['quote'], f['summary'], str(f['relevance']),
                    f['system'], f['location'], f['eff'], f['eff_prov'], f['p'], f['p_prov'],
                    f['n'], f['n_prov'], str(f['class']), STRENGTH[f['strength']]]
            for ci, v in enumerate(vals, 5):
                ws.cell(r, ci, v)
            r += 1
            counts['findings'] += 1
            counts['against'] += bool(f.get('against'))
    m = wb['Method']
    for row in range(1, 8):
        label = m.cell(row, 1).value
        m.cell(row, 2, METHOD[label])
    wb.save(OUT)
    print(OUT, counts)


if __name__ == '__main__':
    main(sys.argv[1:] or ORDER)
