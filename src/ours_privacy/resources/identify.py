# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import identify_create_or_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.identify_create_or_update_response import IdentifyCreateOrUpdateResponse

__all__ = ["IdentifyResource", "AsyncIdentifyResource"]


class IdentifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ours-privacy-python#accessing-raw-response-data-eg-headers
        """
        return IdentifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ours-privacy-python#with_streaming_response
        """
        return IdentifyResourceWithStreamingResponse(self)

    def create_or_update(
        self,
        *,
        token: str,
        user_properties: identify_create_or_update_params.UserProperties,
        default_properties: Optional[identify_create_or_update_params.DefaultProperties] | Omit = omit,
        email: Optional[str] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentifyCreateOrUpdateResponse:
        """Define visitor properties on an existing visitor or create a new visitor.

        Note:
        This does not fire an event. If you want to fire an event, use the track method
        and include properties for the visitor.

        Args:
          token: The token for your Ours Privacy Source. You can find this in the Ours dashboard.

          user_properties: User properties to associate with this user. The existing user properties will
              be updated. And all future events will have these properties associated with
              them.

          default_properties: These properties are used throughout the Ours app to pass known values onto
              destinations

          email: The email address of a user. We will associate this event with the user or
              create a user. Used for lookup if externalId and userId are not included in the
              request.

          external_id: The externalId (the ID in your system) of a user. We will associate this event
              with the user or create a user. If included in the request, email lookup is
              ignored.

          user_id: The Ours user id stored in local storage and cookies on your web properties. If
              userId is included in the request, we do not lookup the user by email or
              externalId.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/identify" if self._client._base_url_overridden else "https://api.oursprivacy.com/api/v1/identify",
            body=maybe_transform(
                {
                    "token": token,
                    "user_properties": user_properties,
                    "default_properties": default_properties,
                    "email": email,
                    "external_id": external_id,
                    "user_id": user_id,
                },
                identify_create_or_update_params.IdentifyCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentifyCreateOrUpdateResponse,
        )


class AsyncIdentifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ours-privacy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ours-privacy-python#with_streaming_response
        """
        return AsyncIdentifyResourceWithStreamingResponse(self)

    async def create_or_update(
        self,
        *,
        token: str,
        user_properties: identify_create_or_update_params.UserProperties,
        default_properties: Optional[identify_create_or_update_params.DefaultProperties] | Omit = omit,
        email: Optional[str] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentifyCreateOrUpdateResponse:
        """Define visitor properties on an existing visitor or create a new visitor.

        Note:
        This does not fire an event. If you want to fire an event, use the track method
        and include properties for the visitor.

        Args:
          token: The token for your Ours Privacy Source. You can find this in the Ours dashboard.

          user_properties: User properties to associate with this user. The existing user properties will
              be updated. And all future events will have these properties associated with
              them.

          default_properties: These properties are used throughout the Ours app to pass known values onto
              destinations

          email: The email address of a user. We will associate this event with the user or
              create a user. Used for lookup if externalId and userId are not included in the
              request.

          external_id: The externalId (the ID in your system) of a user. We will associate this event
              with the user or create a user. If included in the request, email lookup is
              ignored.

          user_id: The Ours user id stored in local storage and cookies on your web properties. If
              userId is included in the request, we do not lookup the user by email or
              externalId.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/identify" if self._client._base_url_overridden else "https://api.oursprivacy.com/api/v1/identify",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "user_properties": user_properties,
                    "default_properties": default_properties,
                    "email": email,
                    "external_id": external_id,
                    "user_id": user_id,
                },
                identify_create_or_update_params.IdentifyCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentifyCreateOrUpdateResponse,
        )


class IdentifyResourceWithRawResponse:
    def __init__(self, identify: IdentifyResource) -> None:
        self._identify = identify

        self.create_or_update = to_raw_response_wrapper(
            identify.create_or_update,
        )


class AsyncIdentifyResourceWithRawResponse:
    def __init__(self, identify: AsyncIdentifyResource) -> None:
        self._identify = identify

        self.create_or_update = async_to_raw_response_wrapper(
            identify.create_or_update,
        )


class IdentifyResourceWithStreamingResponse:
    def __init__(self, identify: IdentifyResource) -> None:
        self._identify = identify

        self.create_or_update = to_streamed_response_wrapper(
            identify.create_or_update,
        )


class AsyncIdentifyResourceWithStreamingResponse:
    def __init__(self, identify: AsyncIdentifyResource) -> None:
        self._identify = identify

        self.create_or_update = async_to_streamed_response_wrapper(
            identify.create_or_update,
        )
