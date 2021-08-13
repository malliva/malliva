import React, { useState } from 'react';
import { Switch } from '@headlessui/react';

import './market-app-user-rights.module.scss';

/* eslint-disable-next-line */
export interface MarketAppUserRightsProps {}

function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}

export function MarketAppUserRights(props: MarketAppUserRightsProps) {
  const [
    allowNewUserSignUpFromInvite,
    setAllowNewUserSignUpFromInvite,
  ] = useState(false);

  const [
    allowAllRegisteredUserToInviteNewUsers,
    setAllowAllRegisteredUserToInviteNewUsers,
  ] = useState(false);

  const [
    allowUsersToMessageEachOther,
    setAllowUsersToMessageEachOther,
  ] = useState(false);

  const [
    allowOnlyVerifiedUsersToPostListing,
    setAllowOnlyVerifiedUsersToPostListing,
  ] = useState(false);

  return (
    <div className="lg:grid grid-cols-12 lg:block lg:col-span-9 xl:col-span-9 lg:gap-8">
      <div className="lg:col-span-12 xl:col-span-12">
        <div className="bg-white px-4 py-5 border-b border-gray-200 sm:px-6">
          <h3 className="text-3xl leading-6 font-medium text-gray-900">
            User rights
          </h3>
        </div>
        <div>
          <div className="m-4">
            <p className="text-xl py-4">Invitation rights</p>
            <div className="m-2">
              <Switch
                checked={allowNewUserSignUpFromInvite}
                onChange={setAllowNewUserSignUpFromInvite}
                className={classNames(
                  allowNewUserSignUpFromInvite
                    ? 'bg-indigo-600'
                    : 'bg-gray-200',
                  'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                )}
              >
                <span className="sr-only">Use setting</span>
                <span
                  aria-hidden="true"
                  className={classNames(
                    allowNewUserSignUpFromInvite
                      ? 'translate-x-5'
                      : 'translate-x-0',
                    'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                  )}
                />
              </Switch>
              Allow new users to sign up only with an invite from a registered
              user
            </div>
            <div className="m-2">
              <Switch
                checked={allowAllRegisteredUserToInviteNewUsers}
                onChange={setAllowAllRegisteredUserToInviteNewUsers}
                className={classNames(
                  allowAllRegisteredUserToInviteNewUsers
                    ? 'bg-indigo-600'
                    : 'bg-gray-200',
                  'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                )}
              >
                <span className="sr-only">Use setting</span>
                <span
                  aria-hidden="true"
                  className={classNames(
                    allowAllRegisteredUserToInviteNewUsers
                      ? 'translate-x-5'
                      : 'translate-x-0',
                    'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                  )}
                />
              </Switch>
              Allow all registered users, and not only admins, to invite new
              users
            </div>
          </div>

          <div className="m-4">
            <p className="text-xl py-4">Communication rights</p>
            <div>
              <Switch
                checked={allowUsersToMessageEachOther}
                onChange={setAllowUsersToMessageEachOther}
                className={classNames(
                  allowUsersToMessageEachOther
                    ? 'bg-indigo-600'
                    : 'bg-gray-200',
                  'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                )}
              >
                <span className="sr-only">Use setting</span>
                <span
                  aria-hidden="true"
                  className={classNames(
                    allowUsersToMessageEachOther
                      ? 'translate-x-5'
                      : 'translate-x-0',
                    'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                  )}
                />
              </Switch>
              Allow users to message each other freely
            </div>
          </div>

          <div className="m-4">
            <p className="text-xl py-4">Posting rights</p>
            <div className="my-8">
              <Switch
                checked={allowOnlyVerifiedUsersToPostListing}
                onChange={setAllowOnlyVerifiedUsersToPostListing}
                className={classNames(
                  allowOnlyVerifiedUsersToPostListing
                    ? 'bg-indigo-600'
                    : 'bg-gray-200',
                  'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                )}
              >
                <span className="sr-only">Use setting</span>
                <span
                  aria-hidden="true"
                  className={classNames(
                    allowOnlyVerifiedUsersToPostListing
                      ? 'translate-x-5'
                      : 'translate-x-0',
                    'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                  )}
                />
              </Switch>
              Allow only users verified by admins to post listings
              <div className="m-3">
                Help users understand what is required to be allowed to post
                listings on your marketplace. These instructions will be
                displayed on the new listing form only to users who aren't
                allowed to post listings.
              </div>
              <div className="my-4">
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-gray-700"
                >
                  Posting rights information text
                </label>
                <div className="mt-1">
                  <textarea
                    name="text"
                    id="post-instruction"
                    className="resize border rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                    placeholder="Posting instruction"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

        <button
          type="button"
          className="w-2/12 flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Save changes
        </button>
      </div>
    </div>
  );
}

export default MarketAppUserRights;
