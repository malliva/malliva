import React, { useEffect } from 'react';

import './market-app-manage-users.module.scss';
import {
  CheckIcon,
  ChevronRightIcon,
  ClockIcon,
  DotsVerticalIcon,
  DuplicateIcon,
  HomeIcon,
  PencilAltIcon,
  SelectorIcon,
  TrashIcon,
  UserAddIcon,
  ViewListIcon,
  LockClosedIcon,
} from '@heroicons/react/solid';
import { XIcon } from '@heroicons/react/outline';

import { Fragment, useState } from 'react';
import { Dialog, Listbox, Menu, Transition } from '@headlessui/react';
import { useDispatch, useSelector } from 'react-redux';
import {
  getCookieForUsersPageTheme,
  getRegisteredUsers,
} from '@client/shared/account-syn-api';
import { selectRegisteredStateStateLoaded } from './market-app-manage-users.slice';
import moment from 'moment';

const people = [
  { id: 1, name: 'Wade Cooper' },
  { id: 2, name: 'Arlene Mccoy' },
  { id: 3, name: 'Devon Webb' },
  { id: 4, name: 'Tom Cook' },
  { id: 5, name: 'Tanya Fox' },
  { id: 6, name: 'Hellen Schmidt' },
  { id: 7, name: 'Caroline Schultz' },
  { id: 8, name: 'Mason Heaney' },
  { id: 9, name: 'Claudie Smitham' },
  { id: 10, name: 'Emil Schaefer' },
];

const navigation = [
  { name: 'Home', href: '#', icon: HomeIcon, current: true },
  { name: 'My tasks', href: '#', icon: ViewListIcon, current: false },
  { name: 'Recent', href: '#', icon: ClockIcon, current: false },
];
const teams = [
  { name: 'Engineering', href: '#', bgColorClass: 'bg-indigo-500' },
  { name: 'Human Resources', href: '#', bgColorClass: 'bg-green-500' },
  { name: 'Customer Success', href: '#', bgColorClass: 'bg-yellow-500' },
];
const projects = [
  {
    id: 1,
    title: 'GraphQL API',
    initials: 'GA',
    team: 'Engineering',
    members: [
      {
        name: 'Dries Vincent',
        handle: 'driesvincent',
        imageUrl:
          'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
      },
      {
        name: 'Lindsay Walton',
        handle: 'lindsaywalton',
        imageUrl:
          'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
      },
      {
        name: 'Courtney Henry',
        handle: 'courtneyhenry',
        imageUrl:
          'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
      },
      {
        name: 'Tom Cook',
        handle: 'tomcook',
        imageUrl:
          'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
      },
    ],
    totalMembers: 12,
    lastUpdated: 'March 17, 2020',
    pinned: true,
    bgColorClass: 'bg-pink-600',
  },
  // More projects...
];

function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}
/* eslint-disable-next-line */
export interface MarketAppManageUsersProps {}

export function MarketAppManageUsers(props: MarketAppManageUsersProps) {
  const dispatch = useDispatch();
  const { response } = useSelector(selectRegisteredStateStateLoaded);

  const [selected, setSelected] = useState(people[3]);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const formatDate = (date) => {
    const formatedDate = moment(date).format('LL');
    return formatedDate;
  };

  useEffect(() => {
    const cookie = getCookieForUsersPageTheme('jwt');
    const parsedJwt = JSON.parse(cookie);
    dispatch(getRegisteredUsers(parsedJwt));
  }, [dispatch]);

  return (
    <div className="lg:grid grid-cols-12 lg:block lg:col-span-9 xl:col-span-9 lg:gap-8">
      <div className="lg:col-span-12 xl:col-span-12">
        <div className="flex items-center justify-between">
          <div className="relative w-6/12">
            <label htmlFor="email" className="sr-only">
              Email
            </label>
            <input
              type="text"
              name="email"
              id="email"
              className="w-full p-2 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block sm:text-sm border-gray-300 rounded-md"
              placeholder="you@example.com"
            />

            <span className="absolute right-0 top-2">
              <XIcon
                className="mr-3 h-5 w-5 text-gray-400"
                aria-hidden="true"
              />
            </span>
          </div>

          <div className="w-3/12">
            <Listbox value={selected} onChange={setSelected}>
              {({ open }) => (
                <>
                  {/* <Listbox.Label className="block text-sm font-medium text-gray-700">
                Roles
              </Listbox.Label> */}
                  <div className="mt-1 relative">
                    <Listbox.Button className="relative w-full bg-white border border-gray-300 rounded-md shadow-sm pl-3 pr-10 py-2 text-left cursor-default focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                      <span className="block truncate">{selected.name}</span>
                      <span className="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none">
                        <SelectorIcon
                          className="h-5 w-5 text-gray-400"
                          aria-hidden="true"
                        />
                      </span>
                    </Listbox.Button>

                    <Transition
                      show={open}
                      as={Fragment}
                      leave="transition ease-in duration-100"
                      leaveFrom="opacity-100"
                      leaveTo="opacity-0"
                    >
                      <Listbox.Options
                        static
                        className="absolute z-10 mt-1 w-full bg-white shadow-lg max-h-60 rounded-md py-1 text-base ring-1 ring-black ring-opacity-5 overflow-auto focus:outline-none sm:text-sm"
                      >
                        {people.map((person) => (
                          <Listbox.Option
                            key={person.id}
                            className={({ active }) =>
                              classNames(
                                active
                                  ? 'text-white bg-indigo-600'
                                  : 'text-gray-900',
                                'cursor-default select-none relative py-2 pl-8 pr-4'
                              )
                            }
                            value={person}
                          >
                            {({ selected, active }) => (
                              <>
                                <span
                                  className={classNames(
                                    selected ? 'font-semibold' : 'font-normal',
                                    'block truncate'
                                  )}
                                >
                                  {person.name}
                                </span>

                                {selected ? (
                                  <span
                                    className={classNames(
                                      active ? 'text-white' : 'text-indigo-600',
                                      'absolute inset-y-0 left-0 flex items-center pl-1.5'
                                    )}
                                  >
                                    <CheckIcon
                                      className="h-5 w-5"
                                      aria-hidden="true"
                                    />
                                  </span>
                                ) : null}
                              </>
                            )}
                          </Listbox.Option>
                        ))}
                      </Listbox.Options>
                    </Transition>
                  </div>
                </>
              )}
            </Listbox>
          </div>

          <div className="auto">
            <button
              type="button"
              className="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-purple-600 hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 sm:order-1 sm:ml-3"
            >
              Export as CSV
            </button>
          </div>
        </div>

        {/* Table users */}
        <div className="">
          <div className="h-screen flex overflow-hidden bg-white">
            <Transition.Root show={sidebarOpen} as={Fragment}>
              <Dialog
                as="div"
                static
                className="fixed inset-0 flex z-40 lg:hidden"
                open={sidebarOpen}
                onClose={setSidebarOpen}
              >
                <Transition.Child
                  as={Fragment}
                  enter="transition-opacity ease-linear duration-300"
                  enterFrom="opacity-0"
                  enterTo="opacity-100"
                  leave="transition-opacity ease-linear duration-300"
                  leaveFrom="opacity-100"
                  leaveTo="opacity-0"
                >
                  <Dialog.Overlay className="fixed inset-0 bg-gray-600 bg-opacity-75" />
                </Transition.Child>
                <Transition.Child
                  as={Fragment}
                  enter="transition ease-in-out duration-300 transform"
                  enterFrom="-translate-x-full"
                  enterTo="translate-x-0"
                  leave="transition ease-in-out duration-300 transform"
                  leaveFrom="translate-x-0"
                  leaveTo="-translate-x-full"
                >
                  <div className="relative flex-1 flex flex-col max-w-xs w-full pt-5 pb-4 bg-white">
                    <Transition.Child
                      as={Fragment}
                      enter="ease-in-out duration-300"
                      enterFrom="opacity-0"
                      enterTo="opacity-100"
                      leave="ease-in-out duration-300"
                      leaveFrom="opacity-100"
                      leaveTo="opacity-0"
                    >
                      <div className="absolute top-0 right-0 -mr-12 pt-2">
                        <button
                          className="ml-1 flex items-center justify-center h-10 w-10 rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                          onClick={() => setSidebarOpen(false)}
                        >
                          <span className="sr-only">Close sidebar</span>
                          <XIcon
                            className="h-6 w-6 text-white"
                            aria-hidden="true"
                          />
                        </button>
                      </div>
                    </Transition.Child>
                    <div className="flex-shrink-0 flex items-center px-4">
                      <img
                        className="h-8 w-auto"
                        src="https://tailwindui.com/img/logos/workflow-logo-purple-500-mark-gray-700-text.svg"
                        alt="Workflow"
                      />
                    </div>
                    <div className="mt-5 flex-1 h-0 overflow-y-auto">
                      <nav className="px-2">
                        <div className="space-y-1">
                          {navigation.map((item) => (
                            <a
                              key={item.name}
                              href={item.href}
                              className={classNames(
                                item.current
                                  ? 'bg-gray-100 text-gray-900'
                                  : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50',
                                'group flex items-center px-2 py-2 text-base leading-5 font-medium rounded-md'
                              )}
                              aria-current={item.current ? 'page' : undefined}
                            >
                              <item.icon
                                className={classNames(
                                  item.current
                                    ? 'text-gray-500'
                                    : 'text-gray-400 group-hover:text-gray-500',
                                  'mr-3 flex-shrink-0 h-6 w-6'
                                )}
                                aria-hidden="true"
                              />
                              {item.name}
                            </a>
                          ))}
                        </div>
                        <div className="mt-8">
                          <h3
                            className="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider"
                            id="teams-headline"
                          >
                            Teams
                          </h3>
                          <div
                            className="mt-1 space-y-1"
                            role="group"
                            aria-labelledby="teams-headline"
                          >
                            {teams.map((team) => (
                              <a
                                key={team.name}
                                href={team.href}
                                className="group flex items-center px-3 py-2 text-base leading-5 font-medium text-gray-600 rounded-md hover:text-gray-900 hover:bg-gray-50"
                              >
                                <span
                                  className={classNames(
                                    team.bgColorClass,
                                    'w-2.5 h-2.5 mr-4 rounded-full'
                                  )}
                                  aria-hidden="true"
                                />
                                <span className="truncate">{team.name}</span>
                              </a>
                            ))}
                          </div>
                        </div>
                      </nav>
                    </div>
                  </div>
                </Transition.Child>
                <div className="flex-shrink-0 w-14" aria-hidden="true">
                  {/* Dummy element to force sidebar to shrink to fit close icon */}
                </div>
              </Dialog>
            </Transition.Root>

            {/* Main column */}
            <div className="flex flex-col w-0 flex-1 overflow-hidden">
              <main className="flex-1 relative z-0 overflow-y-auto focus:outline-none">
                {/* Projects list (only on smallest breakpoint) */}
                <div className="mt-10 sm:hidden">
                  <div className="px-4 sm:px-6">
                    <h2 className="text-gray-500 text-xs font-medium uppercase tracking-wide">
                      Users
                    </h2>
                  </div>
                  <ul className="mt-3 border-t border-gray-200 divide-y divide-gray-100">
                    {response.length > 0 &&
                      response.map((project) => (
                        <li key={project._id}>
                          <a
                            href="#"
                            className="group flex items-center justify-between px-4 py-4 hover:bg-gray-50 sm:px-6"
                          >
                            <span className="flex items-center truncate space-x-3">
                              <span
                                className={classNames(
                                  'bg-pink-600',
                                  //project.bgColorClass,
                                  'w-2.5 h-2.5 flex-shrink-0 rounded-full'
                                )}
                                aria-hidden="true"
                              />
                              <span className="font-medium truncate text-sm leading-6">
                                {project.first_name} {project.last_name}
                              </span>
                            </span>
                            <ChevronRightIcon
                              className="ml-4 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                              aria-hidden="true"
                            />
                          </a>
                        </li>
                      ))}
                  </ul>
                </div>

                {/* Projects table (small breakpoint and up) */}
                <div className="hidden mt-8 sm:block">
                  <div className="align-middle inline-block min-w-full border-b border-gray-200">
                    <table className="min-w-full">
                      <thead>
                        <tr className="border-t border-gray-200">
                          <th className="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            <span className="lg:pl-2">Name</span>
                          </th>
                          <th className="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Email
                          </th>
                          <th className="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Admin
                          </th>
                          <th className="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Created_at
                          </th>
                          <th className="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Post
                          </th>
                          <th className="pr-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Action
                          </th>
                        </tr>
                      </thead>
                      <tbody className="bg-white divide-y divide-gray-100">
                        {response.length > 0 &&
                          response.map((project) => (
                            <tr key={project._id}>
                              <td className="px-6 py-3 max-w-0  whitespace-nowrap text-sm font-medium text-gray-900">
                                <div className="flex items-center space-x-3 lg:pl-2">
                                  <div
                                    className={classNames(
                                      'bg-pink-600',
                                      'flex-shrink-0 w-2.5 h-2.5 rounded-full'
                                    )}
                                    aria-hidden="true"
                                  />
                                  <a
                                    href="#"
                                    className="truncate hover:text-gray-600"
                                  >
                                    <span>
                                      {project.first_name} {project.last_name}
                                    </span>
                                  </a>
                                </div>
                              </td>

                              <td className="px-6 py-3 max-w-0  whitespace-nowrap text-sm font-medium text-gray-900">
                                <span>{project.email}</span>
                              </td>

                              <td className="px-6 py-3 max-w-0  whitespace-nowrap text-sm font-medium text-gray-900">
                                <span>
                                  {project.is_superuser ? 'True' : 'False'}
                                </span>
                              </td>

                              <td className="hidden md:table-cell px-6 py-3 whitespace-nowrap text-sm text-gray-500 text-left">
                                {formatDate(project.created_at)}
                              </td>

                              <td className="hidden md:table-cell px-6 py-3 whitespace-nowrap text-sm text-gray-500 text-left">
                                <div className="relative flex items-start">
                                  <div className="flex items-center h-5">
                                    <input
                                      id="comments"
                                      aria-describedby="comments-description"
                                      name="comments"
                                      type="checkbox"
                                      className="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                                    />
                                  </div>
                                </div>
                              </td>

                              <td className="pr-6">
                                <Menu
                                  as="div"
                                  className="relative flex justify-start items-center"
                                >
                                  {({ open }) => (
                                    <>
                                      <Menu.Button className="w-8 h-8 bg-white inline-flex items-center justify-center text-gray-400 rounded-full hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500">
                                        <span className="sr-only">
                                          Open options
                                        </span>
                                        <DotsVerticalIcon
                                          className="w-5 h-5"
                                          aria-hidden="true"
                                        />
                                      </Menu.Button>
                                      <Transition
                                        show={open}
                                        as={Fragment}
                                        enter="transition ease-out duration-100"
                                        enterFrom="transform opacity-0 scale-95"
                                        enterTo="transform opacity-100 scale-100"
                                        leave="transition ease-in duration-75"
                                        leaveFrom="transform opacity-100 scale-100"
                                        leaveTo="transform opacity-0 scale-95"
                                      >
                                        <Menu.Items
                                          static
                                          className="mx-3 origin-top-right absolute right-7 top-0 w-48 mt-1 rounded-md shadow-lg z-10 bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-200 focus:outline-none"
                                        >
                                          <div className="py-1">
                                            <Menu.Item>
                                              {({ active }) => (
                                                <a
                                                  href="#"
                                                  className={classNames(
                                                    active
                                                      ? 'bg-gray-100 text-gray-900'
                                                      : 'text-gray-700',
                                                    'group flex items-center px-4 py-2 text-sm'
                                                  )}
                                                >
                                                  <PencilAltIcon
                                                    className="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                                                    aria-hidden="true"
                                                  />
                                                  Edit
                                                </a>
                                              )}
                                            </Menu.Item>
                                            <Menu.Item>
                                              {({ active }) => (
                                                <a
                                                  href="#"
                                                  className={classNames(
                                                    active
                                                      ? 'bg-gray-100 text-gray-900'
                                                      : 'text-gray-700',
                                                    'group flex items-center px-4 py-2 text-sm'
                                                  )}
                                                >
                                                  <DuplicateIcon
                                                    className="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                                                    aria-hidden="true"
                                                  />
                                                  Grant admin rights
                                                </a>
                                              )}
                                            </Menu.Item>
                                          </div>
                                          <div className="py-1">
                                            <Menu.Item>
                                              {({ active }) => (
                                                <a
                                                  href="#"
                                                  className={classNames(
                                                    active
                                                      ? 'bg-gray-100 text-gray-900'
                                                      : 'text-gray-700',
                                                    'group flex items-center px-4 py-2 text-sm'
                                                  )}
                                                >
                                                  <LockClosedIcon
                                                    className="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                                                    aria-hidden="true"
                                                  />
                                                  Disable user account
                                                </a>
                                              )}
                                            </Menu.Item>
                                            <Menu.Item>
                                              {({ active }) => (
                                                <a
                                                  href="#"
                                                  className={classNames(
                                                    active
                                                      ? 'bg-gray-100 text-gray-900'
                                                      : 'text-gray-700',
                                                    'group flex items-center px-4 py-2 text-sm'
                                                  )}
                                                >
                                                  <TrashIcon
                                                    className="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                                                    aria-hidden="true"
                                                  />
                                                  Delete user account
                                                </a>
                                              )}
                                            </Menu.Item>
                                          </div>
                                        </Menu.Items>
                                      </Transition>
                                    </>
                                  )}
                                </Menu>
                              </td>
                            </tr>
                          ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </main>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default MarketAppManageUsers;
