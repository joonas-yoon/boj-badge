# BOJ Badge

![Heroku App Status](https://heroku-shields.herokuapp.com/boj-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/joonas-yoon/boj-badge?color=orange) ![GitHub issues](https://img.shields.io/github/issues/joonas-yoon/boj-badge) ![GitHub](https://img.shields.io/github/license/joonas-yoon/boj-badge)

## Examples

- 랭킹 : ![solved](https://boj-badge.herokuapp.com/?id=joonas&label=BOJ%20rank)
- 맞은 문제 수 : ![solved](https://boj-badge.herokuapp.com/?id=joonas&color=green)
- 맞았지만 만점을 받지 못한 문제: ![psolved](https://boj-badge.herokuapp.com/?id=joonas&label=BOJ%20partial%20solved&query=psolved&color=orange)
- 시도했지만 맞지 못한 문제: ![failed](https://boj-badge.herokuapp.com/?id=joonas&label=BOJ%20unsolved&query=failed&color=red)
- 제출 수 : ![submitted](https://boj-badge.herokuapp.com/?id=joonas&label=custom&query=submitted&color=lightgrey)
- 커스텀 라벨 : ![custom-label](https://boj-badge.herokuapp.com/?id=joonas&label=custom&query=id)
- 여러 가지 색상 : ![color1](https://boj-badge.herokuapp.com/?id=joonas) ![color2](https://boj-badge.herokuapp.com/?id=joonas&color=blue) ![color3](https://boj-badge.herokuapp.com/?id=joonas&color=aqua) ![color5](https://boj-badge.herokuapp.com/?id=joonas&color=purple) ![color6](https://boj-badge.herokuapp.com/?id=joonas&color=yellow) ![color7](https://boj-badge.herokuapp.com/?id=joonas&color=lightgrey) ![color8](https://boj-badge.herokuapp.com/?id=joonas&color=black) ![color9](https://boj-badge.herokuapp.com/?id=joonas&color=%23E68364)

## Quickstart

**Markdown**

```
![BOJ badge](https://boj-badge.herokuapp.com/?id={handle})
```

![BOJ badge](https://boj-badge.herokuapp.com/?id=joonas)

**HTML tag**

```
<img src="https://boj-badge.herokuapp.com/?id={handle}" alt="BOJ badge"/>
```

<img src="https://boj-badge.herokuapp.com/?id=joonas" alt="BOJ badge"/>

### Parameters
```
https://boj-badge.herokuapp.com/?id={handle}&query={query}&color={color}&label={label}
```

- `handle` - 백준 온라인 저지의 유저 아이디
- `query`
- - 아래 6가지 정보만 조회할 수 있습니다. (ex. `/?id={handle}&query=rank`)
- - `id` - **아이디**를 표시합니다.
- - `rank` - **랭킹**을 표시합니다.
- - `solved` - **맞은 문제 수**를 표시합니다.
- - `psolved` - **맞았지만 만점을 받지 못한 문제**를 표시합니다.
- - `failed` - **시도했지만 맞지 못한 문제**를 표시합니다.
- - `submitted` - **제출 수**를 표시합니다.
- `color`
- - ![aqua](https://boj-badge.herokuapp.com/?id=joonas&label=aqua&query=id&color=aqua) ![black](https://boj-badge.herokuapp.com/?id=joonas&label=black&query=id&color=black) ![blue](https://boj-badge.herokuapp.com/?id=joonas&label=blue&query=id&color=blue) ![brightred](https://boj-badge.herokuapp.com/?id=joonas&label=brightred&query=id&color=brightred) ![fuchsia](https://boj-badge.herokuapp.com/?id=joonas&label=fuchsia&query=id&color=fuchsia) ![gray](https://boj-badge.herokuapp.com/?id=joonas&label=gray&query=id&color=gray) ![green](https://boj-badge.herokuapp.com/?id=joonas&label=green&query=id&color=green) ![lightgrey](https://boj-badge.herokuapp.com/?id=joonas&label=lightgrey&query=id&color=lightgrey) ![navy](https://boj-badge.herokuapp.com/?id=joonas&label=navy&query=id&color=navy) ![orange](https://boj-badge.herokuapp.com/?id=joonas&label=orange&query=id&color=orange) ![purple](https://boj-badge.herokuapp.com/?id=joonas&label=purple&query=id&color=purple) ![red](https://boj-badge.herokuapp.com/?id=joonas&label=red&query=id&color=red) ![silver](https://boj-badge.herokuapp.com/?id=joonas&label=silver&query=id&color=silver) ![teal](https://boj-badge.herokuapp.com/?id=joonas&label=teal&query=id&color=teal) ![white](https://boj-badge.herokuapp.com/?id=joonas&label=white&query=id&color=white) ![yellow](https://boj-badge.herokuapp.com/?id=joonas&label=yellow&query=id&color=yellow)
- - Hex code도 가능하지만 `#` 을 `%23` 으로 적어야합니다. (`color=#E68364` => `color=%23E68364`)

## Requirements

- Python 3.8
- PostgreSQL or SQLite

## Install & Run

```
$ pip install -r requirements.txt
$ gunicorn app:app
```

## Development

[Heroku](https://devcenter.heroku.com/articles/git)를 통해서 배포합니다.

이 레포지토리를 fork 한 후, Heroku 계정을 사용하여 직접 배포할 수 있습니다.

- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

## License

