# BOJ Badge

![Heroku App Status](https://heroku-shields.herokuapp.com/boj-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/joonas-yoon/boj-badge?color=orange) ![GitHub issues](https://img.shields.io/github/issues/joonas-yoon/boj-badge) ![GitHub](https://img.shields.io/github/license/joonas-yoon/boj-badge)

## Examples

- 랭킹 : ![rank](https://boj-badge.herokuapp.com/?id=joonas&query=rank) ![rank-a](https://boj-badge.herokuapp.com/?id=joonas&query=rank+b&color=%2300b4fc)
- 문제 수 : ![solved](https://boj-badge.herokuapp.com/?id=joonas&color=%23009874&query=solved+a) ![psolved](https://boj-badge.herokuapp.com/?id=joonas&query=psolved&color=%23efc050) ![failed](https://boj-badge.herokuapp.com/?id=joonas&query=failed&color=red)
- 커스텀 라벨 : ![custom-label](https://boj-badge.herokuapp.com/?id=joonas&label=joonas+solved&query=solved)
- 최장 스트릭 : ![color8](https://boj-badge.herokuapp.com/?id=joonas&color=black&label=BOJ+badge&query=max_streak)
- 여러 가지 색상 : ![color6](https://boj-badge.herokuapp.com/?id=joonas&color=yellow&label=BOJ+badge) ![color7](https://boj-badge.herokuapp.com/?id=joonas&color=lightgrey&label=BOJ+badge) ![color9](https://boj-badge.herokuapp.com/?id=joonas&color=%23E68364&label=BOJ+badge)

## Quickstart

**Markdown**

```
![BOJ badge](https://boj-badge.herokuapp.com/?id={handle})
```

**HTML tag**

```
<img src="https://boj-badge.herokuapp.com/?id={handle}" alt="BOJ badge"/>
```

### Parameters
```
https://boj-badge.herokuapp.com/?id={id}&query={query}&color={color}&label={label}
```

**id**

정보를 조회하려는 백준 온라인 저지의 유저 아이디입니다. 사용법은 `/?id=joonas` 와 같습니다.

**query**

`query`에 따라 조회하는 정보와 결과는 아래와 같습니다. 생략한다면, `solved`를 조회합니다.

`rank`의 경우, `/?id={id}&query=rank` 와 같이 사용하시면 됩니다.

| query | 설명 | 결과 |
| :-- | :-- | :--: |
| `id` | **유저 아이디**를 표시합니다. | ![example-id](https://boj-badge.herokuapp.com/?id=joonas&query=id) |
| `rank` | **등수**를 표시합니다. | ![example-rank](https://boj-badge.herokuapp.com/?id=joonas&query=rank) |
| `rank+a` | **등수**와 **전체 등수**를 표시합니다. | ![example-rank-a](https://boj-badge.herokuapp.com/?id=joonas&query=rank+a) |
| `rank+b` | 등수를 **백분율**로 표시합니다. | ![example-rank-b](https://boj-badge.herokuapp.com/?id=joonas&query=rank+b) |
| `rank+c` | **랭킹 몇 페이지**에 있는 지 표시합니다. (정확하지 않습니다) | ![example-rank-c](https://boj-badge.herokuapp.com/?id=joonas&query=rank+c) |
| `solved` | **맞은 문제 수**를 표시합니다. | ![example-solved](https://boj-badge.herokuapp.com/?id=joonas&query=solved) |
| `solved+a` | **채점 가능한 전체 문제 수**를 함께 표시합니다. | ![example-solved-a](https://boj-badge.herokuapp.com/?id=joonas&query=solved+a) |
| `solved+b` | 맞은 문제 수를 **백분율**로 표시합니다. | ![example-solved-b](https://boj-badge.herokuapp.com/?id=joonas&query=solved+b) |
| `psolved` | **맞았지만 만점을 받지 못한 문제**를 표시합니다. | ![example-psolved](https://boj-badge.herokuapp.com/?id=joonas&query=psolved) |
| `psolved+a` | **채점 가능한 전체 문제 수**를 함께 표시합니다. | ![example-psolved-a](https://boj-badge.herokuapp.com/?id=joonas&query=psolved+a) |
| `psolved+b` | 맞았지만 만점을 받지 못한 문제를 **백분율**로 표시합니다. | ![example-psolved-b](https://boj-badge.herokuapp.com/?id=joonas&query=psolved+b) |
| `failed` | **시도했지만 맞지 못한 문제**를 표시합니다. | ![example-failed](https://boj-badge.herokuapp.com/?id=joonas&query=failed) |
| `failed+a` | **채점 가능한 전체 문제 수**를 함께 표시합니다. | ![example-failed-a](https://boj-badge.herokuapp.com/?id=joonas&query=failed+a) |
| `failed+b` | 시도했지만 맞지 못한 문제를 **백분율**로 표시합니다. | ![example-failed-b](https://boj-badge.herokuapp.com/?id=joonas&query=failed+b) |
| `submitted` | **제출 수**를 표시합니다. | ![example-submitted](https://boj-badge.herokuapp.com/?id=joonas&query=submitted) |
| `max_streak` | 연속으로 문제를 푼 **최장 스트릭**을 표시합니다. | ![example-max_streak](https://boj-badge.herokuapp.com/?id=joonas&query=max_streak) |


**color**

사용 가능한 색상은 아래 표를 참고하시길 바랍니다.

Hex code로 직접 색상을 지정할 수 있습니다. 단, `#` 을 `%23` 으로 적어야합니다. (`color=#E68364` => `color=%23E68364`)

| 색상값 | 결과 |
| :-- | :--: |
| aqua | ![aqua](https://boj-badge.herokuapp.com/?id=joonas&label=aqua&query=id&color=aqua) |
| black | ![black](https://boj-badge.herokuapp.com/?id=joonas&label=black&query=id&color=black) |
| blue | ![blue](https://boj-badge.herokuapp.com/?id=joonas&label=blue&query=id&color=blue) |
| brightred | ![brightred](https://boj-badge.herokuapp.com/?id=joonas&label=brightred&query=id&color=brightred) |
| fuchsia | ![fuchsia](https://boj-badge.herokuapp.com/?id=joonas&label=fuchsia&query=id&color=fuchsia) |
| gray | ![gray](https://boj-badge.herokuapp.com/?id=joonas&label=gray&query=id&color=gray) |
| green | ![green](https://boj-badge.herokuapp.com/?id=joonas&label=green&query=id&color=green) |
| lightgrey | ![lightgrey](https://boj-badge.herokuapp.com/?id=joonas&label=lightgrey&query=id&color=lightgrey) |
| navy | ![navy](https://boj-badge.herokuapp.com/?id=joonas&label=navy&query=id&color=navy) |
| orange | ![orange](https://boj-badge.herokuapp.com/?id=joonas&label=orange&query=id&color=orange) |
| purple | ![purple](https://boj-badge.herokuapp.com/?id=joonas&label=purple&query=id&color=purple) |
| red | ![red](https://boj-badge.herokuapp.com/?id=joonas&label=red&query=id&color=red) |
| silver | ![silver](https://boj-badge.herokuapp.com/?id=joonas&label=silver&query=id&color=silver) |
| teal | ![teal](https://boj-badge.herokuapp.com/?id=joonas&label=teal&query=id&color=teal) |
| white | ![white](https://boj-badge.herokuapp.com/?id=joonas&label=white&query=id&color=white) |
| yellow | ![yellow](https://boj-badge.herokuapp.com/?id=joonas&label=yellow&query=id&color=yellow) |

**label**

label 부분의 텍스트를 직접 지정할 수 있습니다. 생략한다면 `query`에 맞게 채워집니다.

| | 예시 | 결과 |
| :-- | :-- | :--: |
| `label` | `![](https://boj-badge.herokuapp.com/?id=joonas&label=alrogithm-solved&query=solved+a)` | ![](https://boj-badge.herokuapp.com/?id=joonas&label=alrogithm-solved&query=solved+a) |

## Requirements

- Python 3.8
- PostgreSQL or SQLite

## Install & Run

**환경 변수 설정**

```
$ export DATABASE_URL=sqlite:///db.sqlite
```

**설치 및 실행**

```
$ pip install -r requirements.txt
$ gunicorn app:app
```

## Development

[Heroku](https://devcenter.heroku.com/articles/git)를 통해서 배포합니다.

이 레포지토리를 fork 한 후, Heroku 계정을 사용하여 직접 배포할 수 있습니다.

- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

## License

The source code for the site is licensed under the MIT license, which you can find in the MIT-LICENSE.txt file.

All graphical assets are licensed under the Creative Commons Attribution 3.0 Unported License.
