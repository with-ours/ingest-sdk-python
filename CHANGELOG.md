# Changelog

## 1.13.1 (2026-05-01)

Full Changelog: [v1.13.0...v1.13.1](https://github.com/with-ours/ingest-sdk-python/compare/v1.13.0...v1.13.1)

### Chores

* **internal:** reformat pyproject.toml ([d29b44f](https://github.com/with-ours/ingest-sdk-python/commit/d29b44f2dd2075d5c692d5fb118c60732828d23e))

## 1.13.0 (2026-04-29)

Full Changelog: [v1.12.3...v1.13.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.12.3...v1.13.0)

### Features

* **api:** api update ([9409366](https://github.com/with-ours/ingest-sdk-python/commit/9409366c4dc91c5a93602bacd37489778ba283ff))
* **api:** api update ([bfa7176](https://github.com/with-ours/ingest-sdk-python/commit/bfa7176eb0593bcff48068d4eadf36a0bada40ad))
* support setting headers via env ([b981bb5](https://github.com/with-ours/ingest-sdk-python/commit/b981bb57b0971df0d65919c9726eb7e3f0856c46))


### Bug Fixes

* use correct field name format for multipart file arrays ([54b7469](https://github.com/with-ours/ingest-sdk-python/commit/54b746955d4818e7ef3a61b1c5cf15a197f7f9cd))

## 1.12.3 (2026-04-23)

Full Changelog: [v1.12.2...v1.12.3](https://github.com/with-ours/ingest-sdk-python/compare/v1.12.2...v1.12.3)

### Chores

* **internal:** more robust bootstrap script ([5bf93e2](https://github.com/with-ours/ingest-sdk-python/commit/5bf93e277f61f74cd723a1a182fc0058b2013299))

## 1.12.2 (2026-04-18)

Full Changelog: [v1.12.1...v1.12.2](https://github.com/with-ours/ingest-sdk-python/compare/v1.12.1...v1.12.2)

### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([de7fcdb](https://github.com/with-ours/ingest-sdk-python/commit/de7fcdb590a291f4fff8f10b7eedcf980084f951))

## 1.12.1 (2026-04-11)

Full Changelog: [v1.12.0...v1.12.1](https://github.com/with-ours/ingest-sdk-python/compare/v1.12.0...v1.12.1)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([894dfb3](https://github.com/with-ours/ingest-sdk-python/commit/894dfb3b4f3d3aa1a3ca19fd88c3dd250a87f6b2))
* ensure file data are only sent as 1 parameter ([5f2dc9f](https://github.com/with-ours/ingest-sdk-python/commit/5f2dc9f2c8e00cd46ea0a6e4de35cd585926db0d))

## 1.12.0 (2026-03-27)

Full Changelog: [v1.11.4...v1.12.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.11.4...v1.12.0)

### Features

* **api:** api update ([26b36b3](https://github.com/with-ours/ingest-sdk-python/commit/26b36b3de6ebe2a773c320f34e404d7324c8647c))
* **internal:** implement indices array format for query and form serialization ([fd9fa15](https://github.com/with-ours/ingest-sdk-python/commit/fd9fa157ae8850c8610ee19ae8305ee9e09b9857))

## 1.11.4 (2026-03-25)

Full Changelog: [v1.11.3...v1.11.4](https://github.com/with-ours/ingest-sdk-python/compare/v1.11.3...v1.11.4)

### Chores

* **ci:** skip lint on metadata-only changes ([16175d9](https://github.com/with-ours/ingest-sdk-python/commit/16175d98570f9b963d5e33e34126a027913177d4))
* **internal:** update gitignore ([cd86aab](https://github.com/with-ours/ingest-sdk-python/commit/cd86aab4648b7549f6bdbf777631ebb672f5254e))

## 1.11.3 (2026-03-20)

Full Changelog: [v1.11.2...v1.11.3](https://github.com/with-ours/ingest-sdk-python/compare/v1.11.2...v1.11.3)

### Bug Fixes

* sanitize endpoint path params ([b84fee8](https://github.com/with-ours/ingest-sdk-python/commit/b84fee803e5c63d7426d6bbb4460354b913522dc))

## 1.11.2 (2026-03-17)

Full Changelog: [v1.11.1...v1.11.2](https://github.com/with-ours/ingest-sdk-python/compare/v1.11.1...v1.11.2)

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([f069a5a](https://github.com/with-ours/ingest-sdk-python/commit/f069a5a6c09ab24a9513129ff6d5d88f321cc78f))
* **pydantic:** do not pass `by_alias` unless set ([8cfd465](https://github.com/with-ours/ingest-sdk-python/commit/8cfd465d0f053e6a84c76966c087ca9fda38c908))


### Chores

* **internal:** tweak CI branches ([57ea2aa](https://github.com/with-ours/ingest-sdk-python/commit/57ea2aabc88dc9dd59d90bdb92d68df51638c20e))

## 1.11.1 (2026-03-08)

Full Changelog: [v1.11.0...v1.11.1](https://github.com/with-ours/ingest-sdk-python/compare/v1.11.0...v1.11.1)

### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([24d22e1](https://github.com/with-ours/ingest-sdk-python/commit/24d22e13f1be81769f0cdbaa13f272c92dea95f9))

## 1.11.0 (2026-03-05)

Full Changelog: [v1.10.0...v1.11.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.10.0...v1.11.0)

### Features

* **api:** api update ([49f1f9d](https://github.com/with-ours/ingest-sdk-python/commit/49f1f9dd024d34f982ee34e6cc164bad6162f304))

## 1.10.0 (2026-02-25)

Full Changelog: [v1.9.3...v1.10.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.9.3...v1.10.0)

### Features

* **api:** api update ([4739a25](https://github.com/with-ours/ingest-sdk-python/commit/4739a2551dafde2d9ef64c4019e20f4d62ebc693))


### Chores

* **internal:** add request options to SSE classes ([e2c3364](https://github.com/with-ours/ingest-sdk-python/commit/e2c33643659ad8488f474cc9a20916e88a795dc1))
* **internal:** make `test_proxy_environment_variables` more resilient ([75d3c2a](https://github.com/with-ours/ingest-sdk-python/commit/75d3c2a803b2b726160fe3e366f5e77c1c795835))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([ea5257c](https://github.com/with-ours/ingest-sdk-python/commit/ea5257cc776b1799374f132ff18c96c6af2716ad))
* **internal:** remove mock server code ([17dfffc](https://github.com/with-ours/ingest-sdk-python/commit/17dfffce03f27cb6c962d81bf540da628efb308e))
* update mock server docs ([66638c7](https://github.com/with-ours/ingest-sdk-python/commit/66638c7d8c42ca8da72f15b52d1ce0b70a5f7577))

## 1.9.3 (2026-02-13)

Full Changelog: [v1.9.2...v1.9.3](https://github.com/with-ours/ingest-sdk-python/compare/v1.9.2...v1.9.3)

### Chores

* format all `api.md` files ([b0827d6](https://github.com/with-ours/ingest-sdk-python/commit/b0827d6a18f28ed3953a706f0d4554c1ca223839))

## 1.9.2 (2026-02-12)

Full Changelog: [v1.9.1...v1.9.2](https://github.com/with-ours/ingest-sdk-python/compare/v1.9.1...v1.9.2)

### Chores

* **internal:** fix lint error on Python 3.14 ([0ab4c0e](https://github.com/with-ours/ingest-sdk-python/commit/0ab4c0ec9705c46ba7754a15c4ee67554895b804))

## 1.9.1 (2026-02-10)

Full Changelog: [v1.9.0...v1.9.1](https://github.com/with-ours/ingest-sdk-python/compare/v1.9.0...v1.9.1)

### Chores

* **internal:** bump dependencies ([a278b41](https://github.com/with-ours/ingest-sdk-python/commit/a278b416fc9a504b634ebde83099a32dc5346f86))

## 1.9.0 (2026-02-04)

Full Changelog: [v1.8.0...v1.9.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.8.0...v1.9.0)

### Features

* **api:** api update ([22dde0a](https://github.com/with-ours/ingest-sdk-python/commit/22dde0aea55c62a87020fc92d189d57bd2de7c38))

## 1.8.0 (2026-01-30)

Full Changelog: [v1.7.1...v1.8.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.7.1...v1.8.0)

### Features

* **client:** add custom JSON encoder for extended type support ([cba9490](https://github.com/with-ours/ingest-sdk-python/commit/cba9490a32017abd177854e903ac3e75e2f7f5ed))

## 1.7.1 (2026-01-24)

Full Changelog: [v1.7.0...v1.7.1](https://github.com/with-ours/ingest-sdk-python/compare/v1.7.0...v1.7.1)

### Chores

* **ci:** upgrade `actions/github-script` ([cb083e6](https://github.com/with-ours/ingest-sdk-python/commit/cb083e6a9e225acd024d83d98dc57451766f6232))

## 1.7.0 (2026-01-17)

Full Changelog: [v1.6.2...v1.7.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.6.2...v1.7.0)

### Features

* **client:** add support for binary request streaming ([e97222b](https://github.com/with-ours/ingest-sdk-python/commit/e97222b495c603b6ade8b0fa65eb3415d57a413c))


### Chores

* **internal:** update `actions/checkout` version ([ff856a6](https://github.com/with-ours/ingest-sdk-python/commit/ff856a6aaa21212fab8ad90097e5e2c33eac4b1c))

## 1.6.2 (2026-01-06)

Full Changelog: [v1.6.1...v1.6.2](https://github.com/with-ours/ingest-sdk-python/compare/v1.6.1...v1.6.2)

### Chores

* **internal:** codegen related update ([ddea8e7](https://github.com/with-ours/ingest-sdk-python/commit/ddea8e76320dbe32eca79e1c8b37eaf5ea9bac1d))

## 1.6.1 (2025-12-19)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/with-ours/ingest-sdk-python/compare/v1.6.0...v1.6.1)

### Bug Fixes

* use async_to_httpx_files in patch method ([2a7d6d0](https://github.com/with-ours/ingest-sdk-python/commit/2a7d6d058a8319246cb7631fda0c48f14e57a7a3))


### Chores

* **internal:** add `--fix` argument to lint script ([dbd84e6](https://github.com/with-ours/ingest-sdk-python/commit/dbd84e6f66b55d8131170a62a800c6f2f0f9babb))

## 1.6.0 (2025-12-17)

Full Changelog: [v1.5.2...v1.6.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.5.2...v1.6.0)

### Features

* **api:** api update ([450e6a6](https://github.com/with-ours/ingest-sdk-python/commit/450e6a6088abd0be782eda40cdc3f8da7747fff0))

## 1.5.2 (2025-12-17)

Full Changelog: [v1.5.1...v1.5.2](https://github.com/with-ours/ingest-sdk-python/compare/v1.5.1...v1.5.2)

### Chores

* speedup initial import ([ae14513](https://github.com/with-ours/ingest-sdk-python/commit/ae14513fb6fb88118ac0168fb4a69dc04f2d9c36))

## 1.5.1 (2025-12-16)

Full Changelog: [v1.5.0...v1.5.1](https://github.com/with-ours/ingest-sdk-python/compare/v1.5.0...v1.5.1)

### Chores

* **internal:** add missing files argument to base client ([25e312c](https://github.com/with-ours/ingest-sdk-python/commit/25e312c7d8bd11cc47d91370b06f75ae40b3f3c7))

## 1.5.0 (2025-12-11)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.4.0...v1.5.0)

### Features

* **api:** api update ([91aac63](https://github.com/with-ours/ingest-sdk-python/commit/91aac633d408c8e69a066f8d8655d6a49e2348e6))

## 1.4.0 (2025-12-11)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** api update ([550fe42](https://github.com/with-ours/ingest-sdk-python/commit/550fe4268809b1c8317a88527a798b85bf28a1c6))

## 1.3.0 (2025-12-10)

Full Changelog: [v1.2.3...v1.3.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.2.3...v1.3.0)

### Features

* **api:** api update ([9957d63](https://github.com/with-ours/ingest-sdk-python/commit/9957d633b4d913aeb42498e57c305b3b817a355e))

## 1.2.3 (2025-12-09)

Full Changelog: [v1.2.2...v1.2.3](https://github.com/with-ours/ingest-sdk-python/compare/v1.2.2...v1.2.3)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([56b7762](https://github.com/with-ours/ingest-sdk-python/commit/56b7762f847d1e18c47de1c5751f4b5dd3af48ac))


### Chores

* add missing docstrings ([c69a391](https://github.com/with-ours/ingest-sdk-python/commit/c69a39178bb856462f20d19c904c604b83365bf0))

## 1.2.2 (2025-12-03)

Full Changelog: [v1.2.1...v1.2.2](https://github.com/with-ours/ingest-sdk-python/compare/v1.2.1...v1.2.2)

### Chores

* update lockfile ([06565c9](https://github.com/with-ours/ingest-sdk-python/commit/06565c969d21d8d2bca00303f4411bb376fd7214))

## 1.2.1 (2025-11-28)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/with-ours/ingest-sdk-python/compare/v1.2.0...v1.2.1)

### Bug Fixes

* ensure streams are always closed ([0d6b6f0](https://github.com/with-ours/ingest-sdk-python/commit/0d6b6f0f4ad99f46c9815b136f828f210295bc88))


### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([8decd50](https://github.com/with-ours/ingest-sdk-python/commit/8decd50690d7ebc355c7fc7e7b1adbbad2ef7549))

## 1.2.0 (2025-11-22)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** api update ([056fb31](https://github.com/with-ours/ingest-sdk-python/commit/056fb315770479159e447bc14f3514343936fc5e))
* **api:** api update ([1d5b0b9](https://github.com/with-ours/ingest-sdk-python/commit/1d5b0b95d3524f8c213d9387947a7d44c8584955))


### Chores

* add Python 3.14 classifier and testing ([88dcfd9](https://github.com/with-ours/ingest-sdk-python/commit/88dcfd9a234ee59926b2b0127b4d3d0b9e3d6be8))

## 1.1.0 (2025-11-19)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/with-ours/ingest-sdk-python/compare/v1.0.1...v1.1.0)

### Features

* **api:** manual updates ([308f0b9](https://github.com/with-ours/ingest-sdk-python/commit/308f0b98f72db1d25da612a267012a29484bfc97))


### Bug Fixes

* compat with Python 3.14 ([cd383a5](https://github.com/with-ours/ingest-sdk-python/commit/cd383a547755f9f4d2bead67e0e550182acdd058))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([88a2708](https://github.com/with-ours/ingest-sdk-python/commit/88a2708fdf7677fd6f247801f1010dc5beaba4af))


### Chores

* **package:** drop Python 3.8 support ([2efe742](https://github.com/with-ours/ingest-sdk-python/commit/2efe7425d8e2ede324289b0355586f0b8608de6d))

## 1.0.1 (2025-11-05)

Full Changelog: [v0.0.1...v1.0.1](https://github.com/with-ours/ingest-sdk-python/compare/v0.0.1...v1.0.1)

### Features

* **api:** manual updates ([bb8c874](https://github.com/with-ours/ingest-sdk-python/commit/bb8c8740c8db117eea1397087a1c6caf84dc9f4f))
* **api:** manual updates ([2fb7a18](https://github.com/with-ours/ingest-sdk-python/commit/2fb7a189d3d85379b026eda316d0941895bf523e))


### Chores

* configure new SDK language ([57f5f26](https://github.com/with-ours/ingest-sdk-python/commit/57f5f26caf7d784f70bf2aa313030c64c4404e5a))
* **internal:** grammar fix (it's -&gt; its) ([fcb2e5a](https://github.com/with-ours/ingest-sdk-python/commit/fcb2e5a28fc12b5d828409f474936d5300e5abf4))
* update SDK settings ([23d204c](https://github.com/with-ours/ingest-sdk-python/commit/23d204c23a68376a0340d1fa6dc160477fe9dd11))
* update SDK settings ([f53800e](https://github.com/with-ours/ingest-sdk-python/commit/f53800e088f0068679c32bd7656dc75e74b9a727))
