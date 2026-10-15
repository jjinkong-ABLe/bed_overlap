# bed_overlap

Python 3.11 이상 표준 라이브러리만 사용하는 생물정보학 CLI입니다. AI 도움을 받아 작성했으며 예제는 합성 자료입니다.

## 실행

```console
python bed_overlap.py examples/a.bed examples/b.bed
python -m unittest -v
```

결과는 표준 출력으로 내보냅니다. 파일로 저장하려면 `> results.txt`를 붙이세요. 잘못된 입력은 오류 메시지와 종료 코드 2로 반환합니다.

## 1. BED 교집합

BED3 이상, 탭 구분, `0 <= start < end`인 0-based half-open 좌표만 지원합니다. 끝과 시작이 닿기만 한 구간은 교집합이 없습니다. 모든 겹치는 입력 행 쌍을 출력하며 중복 입력도 별도 행으로 취급합니다. 이름은 선택하지 않고 원본 줄 번호로 식별합니다. 염색체 이름이 완전히 같아야 비교합니다. Strand·BED12 블록은 해석하지 않습니다. 작은 자료용 구현이며 최악의 경우 O(A×B)여서 대규모 자료에는 bedtools 등을 권장합니다.

[UCSC BED 형식](https://genome.ucsc.edu/FAQ/FAQformat#format1)

